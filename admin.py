from django.admin import admin
from .models import Menu, Orders, OrderItem


@admin.register(Menu)
class MenuAdmin(admin.AdminModel):
    list_display = ('name','category','price')
    search_fields = ('name','category')

@admin.register(Order)
class OrderAdmin(admin.AdminModel):
    list_display = ('id','customer','status','total_amount','ordered_at')
    list_filter = ('status','ordered_at')
    search_fields = ('customer__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.AdminModel):
    list_display = ('order','menu_item','quantity')

