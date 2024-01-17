from rest_framework import serializers
from rongry.models import Category, Product, User, Post, Wishlist,  Subscribers, Testimonial


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'price', 'description']


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    # def validate_name(self, value):
    #    if User.objects.filter(username=value).exists():
    #       KeyError
    #     return value
    

        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
      model = Category
      fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
      model = Post
      fields = ['pk','title', 'slug', 'content', 'overview','timestamp','thumbnail','categories','owner']
      # read_only_fields=['overview','timestamp','thumbnail','categories','owner']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
      model = Wishlist
      fields = '__all__'

class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
      model = Subscribers
      fields = '__all__'

class TestimonalSerializer(serializers.ModelSerializer):
   class Meta:
      model= Testimonial
      fields = '__all__'





