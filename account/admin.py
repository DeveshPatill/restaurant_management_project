from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
# Register your models here.

class Menu(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending','pending'),
        ('Confirmed','confirmed'),
        ('Delivered','delivered'),
        ('Cancelled','cancelled'),
    ]
    order_items = models.ManyToManyField(Menu, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits= 8,decimal_places= 2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.customer.username}"

class OrderItem(models.Model):
    order = models.Foreignkey(Order, on_delete.models.CASCADE)
    menu_item = models.Foreignkey(Menu, on_delete.models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} (Order #{self.order.pk})"