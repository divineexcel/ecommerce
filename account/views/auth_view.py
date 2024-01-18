from rest_framework.generics import CreateAPIView

from account.serializers import LoginSerializer, LoginResponseSerializer, RegisterSerializer, RegisterResponseSerializer
from services.auth_service import AuthService
from services.response_service import ResponseService


class LoginView(CreateAPIView, ResponseService):
    permission_classes = []
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        service = AuthService(request)

        serializer = self.serializer_class(request.data)
        if serializer.is_valid():

            data, error = service.login(
                serializer.validated_data
            )

            if error:
                return self.send_bad_request(error)

            return self.send_json({
                "data": LoginResponseSerializer(data).data
            })
        else:
            return self.send_validation_error(serializer.errors)


class RegistrationView(CreateAPIView, ResponseService):
    permission_classes = []
    authentication_classes = []
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        service = AuthService(request)

        serializer = self.serializer_class(request.data)
        if serializer.is_valid():

            data, error = service.register_user(
                serializer.validated_data
            )

            if error:
                return self.send_bad_request(error)

            return self.send_json({
                "data": RegisterResponseSerializer(data).data
            })

        else:
            return self.send_validation_error(serializer.errors)
