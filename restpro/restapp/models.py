from django.db import models

# Create your models here.

class Order(models.Model):
    order =models.CharField(max_length=30)
    customers =models.CharField(max_length=30)
    total_orders =models.IntegerField(max_length=30)
    delivered =models.IntegerField(max_length=30)
    pending =models.IntegerField(max_length=30)

class Product():
    pass

class Customer():
    pass