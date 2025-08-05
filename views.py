from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decimal import Decimal
from django.shortcuts import render
from .models import MenuItem

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