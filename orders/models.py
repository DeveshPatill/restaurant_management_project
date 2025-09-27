from django.db import models
from django.conf import settings
from home.models import Product

# Create your models here.
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Orderstatus

@receiver(post_migrate)
def create_default_statuses(sender, **kwargs):
    if sender.name == "orders":
        for status in Orderstatus.DEFAULT_STATUSES:
            Orderstatus.objects.get_or_create(name=status)

class Orderstatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


    PENDING ="Pending"
    PROCESSING = 'Processing'
    COMPLETED = "Completed"
    CANCELLED = 'Cancelled'

    DEFAULT_STATUSES =[PENDING, PROCESSING, COMPLETED, CANCELLED]

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_length=10, Decimalplaces=2)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(
        Orderstatus,
        on_delete = models.SET_NULL,
        null=True,
        related_name="Orders"
    )

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}({self.status})"

class MenuCategory(models.Model):
    name =models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, Decimalplaces=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    date=models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, Decimalplaces=2)
    items = models.ManyToManyField(Item, related_name="orders")

    def __str__(self):
        return f"Order {self.id} by {self.user.username}

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, Decimalplaces=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ActiveOrderManager(models.Manager):
    def_active_orders(self):
        return super().get_queryset().filter(status__in=['pending','processing'])

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    opening_days = models.CharField(
        max_length=100,
        help_text= "Comma-seperated days (e.g.,Mon ,Tue,Wed,Thu,Fri)"
    )
    
    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(Product, related_name='orders')
    total_price = models.DecimalField(max_digits=10, Decimalplaces=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order {self.order_id} by {self.customer.username}"