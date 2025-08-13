from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decimal import Decimal
from django.shortcuts import render, redirect
from .models import MenuItem
from .models import Restaurant
from django.conf import settings
from django.http import HttpResponse
from .forms import FeedBackForm,MenuItem,ContactForm

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

# added template and defining the custom 404_page view logic here
def error_404_page(request, exception):
    return render(request, '404_page.html', status=404)


#creating a view to display the list of menu_items . using a simple hardcoded list here
def menu_view(request):
    menu_items = [
        {"name":"french fries", "description":"Classic peri-peri fries ", "price":10.22},
        {"name":"Capsicum Pizza", "description":"Classic Chhes Pizza", "price":9.22},
    ]
    return render(request, "menu.html", {"menu_items":menu_items}, status=status.HTTP_200_OK)

#creating the simple django template for homepage , which can display the restaurant name and welcome message
def my_homepage(request):
    context = {
        "restaurant_name" : "My Spicy Restaurant",
        "welcome_message" : "Welcome to our Restaurant, We don't serve meals, we serve Experiences. "
    }
    return render(request, 'homepage.html', context)

# creating the method for contact_us page
def contact_us_page(request):
    return render(request, 'restaurant_management/templates/contact_us.html')


# displaying the restaurants phone number on the homepage with the help of settings.py or models.py
def displaying_Contact(request):
    phone = settings.RESTAURANT_PHONE_NUMBER
    return render(request, 'restaurant_management/templates/homepage.html', {'phone':phone})


# Instead of adding it manually in every view , use a context processor so current_year is available in every template

def current_year(request):
    return {
        'current_year': dateTime.now().year
    }

#basic error handeling in django view
def list_restaurants(request):
    try:
        restaurants_list = Restaurant.objects.all()
        return render(request, 'restaurant_list.html', {'restaurants_list':restaurants_list})
    except Restaurant.DoesNotExist:
        return HttpResponse("No Restaurant Found", status=404)
    except Exception as e:
        print(f"error occurred {e}")
        return HttpResponse("something went wrong. Please, Try again later", status=500)

#view for feedback form 
def feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "feedback_thanks.html")
        else:
            form = FeedBackForm()
            return render(request, 'feedback.html', {'form':form})

#method for opening_hour in footer
def opening_hour(request):
    return {
        'opening_hour' : 'Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm'
    }

# Displaying the restaurant address in homepage.html
def homepage_address(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'homepage.html', {'restaurant_address':restaurant})

# displaying to show menu images and details
def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items':items})


# 
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
        else:
            form = ContactForm()
            return render(request, 'contactForm.html', {'form':form})

def contact_success(request):
    return render(request, 'contact_success.html')
