from django.urls import path
from .views import *

urlpatterns = [
    path("history/",OrderHistoryView.as_View(),name="order-history"),
    
]