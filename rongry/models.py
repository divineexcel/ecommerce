# from typing import List
from django.db import models

# rom commerce.user.serializers import UserRegistrationSerializerf
from django.contrib.auth.models import User, AbstractUser


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True )
    subtitle = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField()
    def __str__(self):
        return self.title    
    

class Product(models.Model):
    name=models.CharField(max_length=200, unique=True)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    image = models.ImageField(null=True,blank=True)
    description=models.CharField(max_length=500,null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return self.name
    
    def __str__(self):
      return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField(null= True , blank= True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    thumbnail = models.ImageField( null=True, blank=True,)
    categories = models.ManyToManyField(Category, null=True, blank= True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)

 
    def __str__(self):
        return self.title


class Wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product}"
    
    # @property
    # def user_first_name(self):
    #     return self.user.first_name
     
class Subscribers(models.Model):
    email=models.EmailField()
    date=models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str :
        return self.email
    

class Testimonial(models.Model): 
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    rating= models.IntegerField
    comment= models.CharField(max_length=40, null=True)
    created= models.DateTimeField(auto_created=True) 
    def __str__(self) -> str:
        return "the rating of" + self.product + "" + str(self.rating)   

# class Sam(List):
#     def __len__(self) -> str:
#         return super().__len__()



    