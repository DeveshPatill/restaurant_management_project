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