"""
URL configuration for restaurant_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('home.urls')),
    path('api/accounts/',include('account.urls')),
    path('api/products/',include('products.urls')),
    path('api/orders/',include('orders.urls')),
    path('menu/', views.menu, name="menu"),
    path('',views.homepage, name="home"),
    path('',views.homepage_view, name = "homepage"),
    path('about/',views.about_us_page, name="about"),
    path('',views.myhomepage, name='homepage'),
    path('contact/',views.contact_us_page, name='contact'),
    path('feedback/',views.feedback, name='feedback'),
    path('contact/',views.contact_view, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('faq/', views.faq_page, name='faq'),
    path('about/', views.about, name='about')
    path('add/<int:item_id/', views.add_to_cart, name="add_to_cart"),
    path("cart/", views.view_cart, name="cart"),
    path("privacy-policy/", views.privacy_policy,name="privacy-policy"),
]
handler404 = "restaurant_management.views.error_404_page"
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
