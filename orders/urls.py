from django.urls import path
from .views import *

urlpatterns = [
    path("history/",OrderHistoryView.as_View(),name="order-history"),
    path('menu-items/',menu_items_by_category, name="menu-items-by-category"),
    
]