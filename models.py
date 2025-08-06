from django.db import models

class Restaurant(models.Model):
    restaurant = models.CharField(max_length=255)

    def __str__(self):
        return self.name