from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to="categories", default="")
       
    def __str__(self):
        return self.category_name

class Product(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255,default="")
    product_price = models.CharField(max_length=255,default="")
    product_image = models.ImageField(upload_to="products",default="")
    is_teends_or_just_arived = models.BooleanField(default=True)
      

    def __str__(self):
        return self.product_name

class UserProfile(models.Model):
    userId = models.OneToOneField(User,on_delete=models.CASCADE, default="")
    user_image = models.ImageField(upload_to="profile")
    phone_number = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=40)
    locality = models.CharField(max_length=50)

    def __str__(self):
        return self.userId.username


