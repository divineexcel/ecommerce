from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from account.serializers import LoginSerializer, LoginResponseSerializer, RegisterSerializer, \
    RegisterResponseSerializer, LogoutSerializer, UserSerializer, RegisterUserSerializer
from services.auth_service import AuthService
from services.response_service import ResponseService
from services.user_service import UserService


class ListOrCreateUsersApiView(ListCreateAPIView, ResponseService):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterUserSerializer

    def get(self, request, *args, **kwargs):

        service = UserService(request)

        filter_keyword = request.GET.get("keyword")
        filter_user_type = request.GET.get("user_type")

        data = service.fetch_users(filter_keyword=filter_keyword, user_type=filter_user_type)
        # note: it is highly inefficient to pull and return all records in situations like this without pagination
        data = UserSerializer(data, many=True).data
        return self.send_json({"data": data})

    def post(self, request, *args, **kwargs):
        service = UserService(request)

        serializer = self.serializer_class(request.data)
        if serializer.is_valid():

            data, error = service.register_user(
                serializer.validated_data
            )

            if error:
                return self.send_bad_request(error)
            return self.send_json(data)
        else:
            return self.send_validation_error(serializer.errors)


class RetrieveUpdateOrDeleteUserApiView(RetrieveUpdateDestroyAPIView, ResponseService):
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


class LogoutView(CreateAPIView, ResponseService):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        service = AuthService(request)

        serializer = self.serializer_class(request.data)

        if serializer.is_valid():
            data, error = service.logout(
                serializer.validated_data
            )

            if error:
                self.send_bad_request(error)

            return data
        else:
            return self.send_validation_error(serializer.errors)
