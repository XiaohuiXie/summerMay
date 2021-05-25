from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
# Create your models here.

class Categories(models.Model):
    category_name = models.CharField(max_length=50,default='Fruits')
    category_added_date = models.DateTimeField(default=timezone.now)

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True,default=1)
    product_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='products')
    created_date = models.DateTimeField(default=timezone.now)
    #category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_name


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    
        
