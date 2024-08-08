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


class CustomUser(models.Model):
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user_image = models.ImageField(upload_to="User")
    pincode = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    user_id = models.OneToOneField(User,on_delete=models.PROTECT,default="")


    def __str__(self):
        return self.user_id.username
