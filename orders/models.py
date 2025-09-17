from django.db import models

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
    total_price = models.DecimalFiels(max_length=10, Decimalplaces=2)
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