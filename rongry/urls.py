from django.contrib import admin
from django.urls import path
# from .views import product, snippet_detail
from rongry import views


urlpatterns = [
    path('products/', views.product),
    path('products/<int:pk>/', views.product_detail),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('subscribe', views.Subscribe.as_view())
    
]
