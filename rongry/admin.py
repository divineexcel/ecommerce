from django.contrib import admin
from .models import  Category, Product, User , Wishlist, Subscribers, Testimonial, Post
 # Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Wishlist)
admin.site.register(Subscribers)
admin.site.register( Testimonial)
admin.site.register( Post)
