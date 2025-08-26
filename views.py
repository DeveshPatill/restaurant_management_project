from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decimal import Decimal
from django.shortcuts import render, redirect
from .models import MenuItem
from .models import Restaurant,Special
from django.conf import settings
from django.http import HttpResponse
from .forms import FeedBackForm,MenuItemForm,ContactForm
from django.core.mail import send_mail

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
        "description": "Since Opening our doors in 1999,My Spicy Restaurant has Delighted guests with bold Flavours, authentic recipies, and a vibrant dining experience. Located in the heart of the city,we specialize in spicy, flavourful dishes inspired by traditional and modern culinary traditions. Our Chefs are passionate about using High-Quality ingredients and handcafted spices to bring every dish to your life.Wheather ur here for casual lunch, a family dinner or a festival celebration, yuo'll find something unforgetable on our menu. At my Spicy Restaurant we just dont serve Food, We Serve Experiences..",
        "image_url":"static/images/restaurant.jpg",
    })

# added template and defining the custom 404_page view logic here
def error_404_page(request, exception):
    return render(request, '404_page.html', status=404)


# creating a view to display the list of menu_items . using a simple hardcoded list here
def menu_view(request):
    menu_items = [
        {"name":"french fries", "description":"Classic peri-peri fries ", "price":10.22},
        {"name":"Capsicum Pizza", "description":"Classic Chhes Pizza", "price":9.22},
    ]
    return render(request, "menu.html", {"menu_items":menu_items}, status=status.HTTP_200_OK)

# creating the simple django template for homepage , which can display the restaurant name and welcome message
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

# view for feedback form 
def feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "feedback_thanks.html")
        else:
            form = FeedBackForm()
            return render(request, 'feedback.html', {'form':form})

# method for opening_hour in footer
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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #form.save()

            #send mail
            send_mail(
                subject=f"New Contact Message From {name}",
                message=f"From {name} <{email}>\n\nMessage:\n{message}",
                from_email=email,
                recipient_list=['patildevesh677@gmail.com'],
            )
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form':form})
    

def contact_success(request):
    return render(request, 'contact_success.html')


# basic search implementation on homepage 
def search_bar(request):
    query = request.get.displaying_Contact('q',' ')
    if query:
        items = MenuItem.objects.filter(name__icontains = query)
    else:
        items = MenuItem.objects.all()
    context = {
        'restaurant_name':'My-Restaurant',
        'phone':'+91 9833142949',
        'restaurant':{'address':'Navi Mumbai, Khoparkhairaine'},
        'welcome_message':'welcome to our restaurant',
        'opening_hours': restaurant.opening_hours if restaurant else {},
        'items':items,
    }
    return render(request, 'homepage.html',context)

def menuview(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu') #reloads page to show new item
    else:
        form = MenuItemForm()
    return render(request, 'menu.html', {'form':form, "menu_items":menu_items})

# displaying the restaurants phonenumber on the home page
def phonenumber(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'home.html', {'restaurant':restaurant})

# dislpaying logo // --> this method is for logo
def logo(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'home.html',{'restaurant':restaurant})



#for displaying total items in cart
def cart_items(request):
    total_items=0
    if request.user.is_authenticated:
        total_items = Cart.objects.filter(user=request.user).count()
    return render(request, 'home.html', {'total_items':total_items})

#FAQ
def faq_page(request):
    return render(request, 'faq.html')
    
#displayb current date and time on the homepage
def homee(request):
    context = {
        "current_time": dateTime.now()
    }
    return render(request, "home.html",context)

#displaying image on about us page
def about(request):
    about_data = About.objects.first()
    return render(request, 'about_us.html', {'about': about_data})


# shopping cart functionality

MENU_ITEMS = {
    1:{"name":"pizza", "price": 10},
    2:{"name":"burger","price": 5},
    3:{"name":"pasta", "price": 8},
}

def menuu(request):
    return render (request, "menu.html", {"menu":MENU_ITEMS})

def add_to_cart(request, item_id):
    cart = request.session.get("cart",{})
    cart[str{item_id}] = cart.get(str(item_id), 0) + 1
    request.session["cart"] = cart #save back to session
    return redirect("view_cart")

def view_cart(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0

    for item_id,qty in cart.items():
        item = MENU_ITEMS[int(item_id)]
        subtotal = item["price"] * qty
        total += subtotal
        cart_items.append({"name":item["name"], "qty":qty, "subtotal":subtotal})
    return render(request, "cart.html", {"cart_items":cart_items, "total":total})


# displaying the specials
def home_(request):
    specials = Special.objects.all()
    return render(request, 'home.html', {"specials":specials})