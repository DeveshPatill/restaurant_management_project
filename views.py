from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decimal import Decimal
from django.shortcuts import render
from .models import MenuItem
from .models import Restaurant
from django.conf import settings

@api_view(['GET'])
def menu_api(request):
    menu = [
        {'name':'Margherita Pizza', 'Description':'Classic Pizza with Tomato Sauce and Mozzarella', 'price': 8.99},
        {'name':'Burger', 'Description':'Spicy Burger with added cheeze and chicken stuffed', 'price': 10},
        {'name':'Korien Noodles', 'Description':'Spicy Noodles', 'price': 12},
    ]
    return Response({"menu":menu}, status=status.HTTP_200_OK) 

# displaying menu items on a dedicated menu page
def menu(request):
    items = MenuItem.objects.all()
    return render(request, "menu.html", {"items":items})


# displaying the restaurants name on the homepage / fetching the name from the setting.py or model [fetched the name from the settings.py here ]

def homepage(request):
    restaurant_name = settings.RESTAURANT_NAME
    return render(request, 'home.html', {'restaurant_name':restaurant_name})

# creating the view to display the restaurant name on the homepage. fetch the name from the model or settings .py [fetched the name from the models.py here]
def get_restaurant_name():
    restaurant = Restaurant.objects.first()
    return restaurant.name if restaurant else settings.RESTAURANT_NAME

def homepage_view(request):
    restaurant_name = get_restaurant_name()
    return render(request, "index.html", {"restaurant_name":restaurant_name})

# for about us page for restaurant includes name, description & image

def about_us_page(request):
    return render(request, "about_us.html",{
        "restaurant_name": get_restaurant_name(),
        "description": "Since Opening our doors in 1999,My Spicy Restaurant has Delighted guests with bold Flavours, authentic recipies, and a vibrant dining experience. Located in the heart of the city,we specialize in spicy, flavourful dishes inspired by traditional and modern culinary traditions. Our Chefs are passionate about using High-Quality ingredients and handcafted spices to bring every dish to your life.Wheather ur here for casual lunch, a family dinner or a festival celebration, yuo'll find something unforgetable on our menu. At my Spicy Restaurant we just dont serve Food, We Serve Experiences.",
        "image_url":"static/images/restaurant.jpg",
    })