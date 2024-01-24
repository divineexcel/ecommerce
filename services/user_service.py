import hashlib
import time
from typing import Any

from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User, UserTypes
from commerce.errors.app_errors import AppLogger
from services.auth_service import AuthService
from services.base_service import BaseService
from services.notification_service import NotificationService


class UserService(BaseService):

    def fetch_users(self, filter_keyword=None, user_type=None) -> (Any, Any):

        q = ~Q(pk=self.request.user.pk)
        if filter_keyword:
            q &= (Q(usernama__icontains=filter_keyword) |
                 Q(first_name__contains=filter_keyword) |
                 Q(last_name__contains=filter_keyword) |
                 Q(email__contains=filter_keyword))
        if user_type:
            q & Q(user_type__iexact=user_type)

        return User.objects.filter(q)

    def generate_random_password(self):
        return hashlib.sha256(str(time.time()).encode('utf8')).hexdigest()

    def register_user(self, payload) -> (Any, Any):
        payload["password"] = self.generate_random_password()
        service = AuthService(self.request)
        return service.register_user(payload, UserTypes.internal_user)

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
        return {
            "refresh_token": str(token),
            "access_token": str(token.access_token)
        }

    def logout(self, payload):
        refresh_token = payload.get("refresh_token")
        response, error = None, None

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            response = {"message": "Successful"}
        except Exception as e:
            error = self.make_error(str(e))
        return response, error
    
    def fetch_single_user(self, username):
        user, error = None, None
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            error = self.make_error(f"User '{username}' does not exist")
        except User.MultipleObjectsReturned:
            error = self.make_error(f"Invalid result found for '{username}'")
        except Exception as e:
            error = self.make_error(str(e))
        return user, error
    

    def update_single_user(self, username):
        user, error = None, None
        try:
            user = User.objects.update(username__iexact=username)
        except User.DoesNotExist:
            error = self.make_error(f"User '{username}' does not exist")
        except Exception as e:
            error = self.make_error(str(e))
        return user, error
    

   
   
    def delete_single_user(self, username):
        user, error = None, None
        try:
            user = User.objects.delete(username__iexact=username)
        except User.DoesNotExist:
            error = self.make_error(f"User '{username}' does not exist")
        except Exception as e:
            error = self.make_error(str(e))
            return user, error