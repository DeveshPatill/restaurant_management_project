from django.contrib import admin
from .models import Menu, Orders, OrderItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','category','price')
    search_fields = ('name','category')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','status','total_amount','ordered_at')
    list_filter = ('status','ordered_at')
    search_fields = ('customer__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','menu_item','quantity')

