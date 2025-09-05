from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.comment}- Feedback #{self.id}"


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    opening_hours = models.JSONField(default=dict)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    logo = models.ImageField(upload_to='restaurant_logos/',null =True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
        
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price  = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(uplaod_to='menu_images/', blank=True, null=True) #image field

    def __str__(self):
        return self.name

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.address} {self.city} {self.state} {self.zip_code}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.name} ({self.quantity})"

class About(models.Model):
    title = models.CharField(max_length=200, default='About Us')
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title

class Special(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class OpeningHour(models.Model):
    day = models.CharField(max_length=200)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.day}: {self.open_time} - {self.close_time}"


class Chef(models.Model):
    name = models.CharField(max_length=225)
    bio = models.TextField()
    image = models.ImageField(upload_to='chefs/')

    def __str__(self):
        return self.name

#python manage.py makemigrations
#python manahe.py migrate