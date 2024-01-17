from django.shortcuts import render
# from django.contrib.auth.models import User
from rongry.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import  JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import UserRegistrationSerializer


# @csrf_exempt
# def register(request) -> JsonResponse:
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         username = data.get("username")
#         password = data.get("password")
#         if User.objects.filter(username=username).exists():
#             return error message

#         user = User.objects.create(username=username)
#         user.set_password(password)
#         authenticate(user, password)
#         login(user)
 

# class Register(APIView):
#     def post(request):
#         data = request.data()

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(user)



def login_view(request):
    data = JSONParser().parse(request)
    username = data.get("username")
    password = data.get("password")
    user = User.objects.filter(username=username).first()
    if not user:
        # return "go and register"
        return JsonResponse ({"error": "go and register"}, status=404)
    

    
    user = authenticate(user, password)
    if user:
        login(user)
    else:
        JsonResponse({"invalid user  password"}, status=404)
        # "invalid user or password"

def logout_view(request):
    logout(request.user)