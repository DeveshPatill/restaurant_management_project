from django.urls import path
from .views import *

urlpatterns = [
    path("history/",OrderHistoryView.as_View(),name="order-history"),
    path('menu-items/',menu_items_by_category, name="menu-items-by-category"),
    path("menu-items/<int:pk>/update/",UpdateMenuItemView.as_view(), name='update-menu-item')
    path("menu-items/search/", MenuItemSearch.as_View(), name="menu-item-search"),
    path('api/profile/update', user_profile_update, name='profile-update',)
    path('coupons/validate/', CouponValidationView.as_View(), name="coupon-validate"),
]