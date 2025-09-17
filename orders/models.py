from django.db import models

# Create your models here.
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Orderstatus

@receiver(post_migrate)
def create_default_statuses(sender, **kwargs):
    if sender.name == "orders":
        for status in Orderstatus.DEFAULT_STATUSES:
            Orderstatus.objects.get_or_create(name=ststus)