from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='products')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.product_name
        
