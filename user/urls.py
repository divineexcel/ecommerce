from django.contrib import admin
from django.urls import path

from . import views
# from .views import product, snippet_detail



urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.login_view),
    path('logout/', views.logout_view)
    
]
