from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to="categories", default="")

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE )
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255 ,default="")
    product_price = models.CharField(max_length=255, default="")
    product_image = models.ImageField(upload_to="products", default="")

    def __str__(self):
        return self.product_name