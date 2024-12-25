from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password



 # Optional: Return user_name as string representation



class Restaurant(models.Model):
    # Fields for restaurant data
    Res_id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=500, null=True, blank=True)
    overall_rating = models.FloatField(null=True, blank=True)
    total_ratings = models.IntegerField(null=True, blank=True)
    price_range = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    max_delivery = models.IntegerField(null=True, blank=True)
    min_delivery = models.IntegerField(null=True, blank=True)
    delivery_time = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    main_location = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.vendor_name  # Return vendor_name as string representation

class Menu(models.Model):
    Item_id = models.AutoField(primary_key=True)  # Unique menu item ID
    Res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menu_items")
    category = models.CharField(max_length=100)  # Menu category, e.g., Burgers, Pizzas
    item = models.CharField(max_length=255)  # Name of the menu item
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return f"{self.item} - {self.Res_id.vendor_name}"