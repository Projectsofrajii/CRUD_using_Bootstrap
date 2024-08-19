from django.db import models

# Create your models here.

class Order(models.Model):
    order =models.CharField(max_length=30)
    customers =models.CharField(max_length=30)
    total_orders =models.IntegerField()
    delivered =models.IntegerField()
    pending =models.IntegerField()

class Product():
    pass

class Customer():
    pass