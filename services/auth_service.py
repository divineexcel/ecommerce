from typing import Any

from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User, UserTypes
from commerce.errors.app_errors import AppLogger
from services.base_service import BaseService
from services.notification_service import NotificationService


class AuthService(BaseService):

    def login(self, payload) -> (Any, Any):

        username = payload.get("username")
        password = payload.get("password")

        authenticate_kwargs = {"username": username, "password": password, "request": self.request}
        login_error_message = "Access denied due to invalid credential"
        try:
            user = authenticate(**authenticate_kwargs)
        except User.MultipleObjectsReturned:
            return None, self.make_error(login_error_message)
        except Exception as e:
            AppLogger.report(e)
            return None, self.make_error(login_error_message)

        if user is None:
            return None, self.make_error(login_error_message)

        if not user.is_active:
            return None, self.make_error("Account is currently not active, contact admin.")

        data = {
            "user": user,
            "user_type": user.user_type,
            "username": user.username,
            "full_name": user.get_full_name(),
            "access_token": self.create_token(user),
        }

        return data, None

    def register_user(self, payload, user_type=None) -> (Any, Any):

        if user_type is None:
            user_type = UserTypes.ordinary_user

        email = payload.get("email")
        username = payload.get("username")
        if self.check_user_with_email_or_username_exists(username=username, email=email):
            return None, self.make_error("User account with email/username already exists")

        try:
            user = User.objects.create_user(
                username=username,
                password=payload.get("password"),
                first_name=payload.get("first_name"),
                last_name=payload.get("last_name"),
                email=email,
                user_type=user_type,
            )
        except Exception as e:
            AppLogger.report(e)
            user = None

        if user is None:
            return None, self.make_error("Unable to complete, try again")

        notification = NotificationService(self.request)
        notification.send_activation_email(user)

        data = {
            "message": f"An activation email has been sent to '{user.email}'. Check your mailbox to proceed.",
            "email": user.email
        }

        return data, None

    def check_user_with_email_or_username_exists(self, username=None, email=None):
        if not username and not email:
            return False

        q = Q()
        if username:
            q |= Q(username__iexact=username)
        if email:
            q |= Q(email__iexact=email)

        return User.objects.filter(q).exists()

    def create_token(self, user):
        token = RefreshToken.for_user(user)
        return str(token.access_token)
