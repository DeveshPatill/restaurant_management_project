from django.db import models

class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id}"


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.
        
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price  = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(uplaod_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name


#python manage.py makemigrations
#python manahe.py migrate