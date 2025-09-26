from rest_framework import serializers
from .models import Order, Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =Item
        fields = ["id", "name","price"]

class OrderSerializer(Serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model =Orderfields =["id","date","total_price","items"]

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields =['id','name','description','price','category','is_available']

        def validate_price(self,value):
            if value <=0:
                raise serializers.alidationError("Price must be a positive number.")
            return value


class UserProfileSerializer(Serializers.ModelSerializer):
    class Meta:
        model = Userfields = ['first_name','last_name','email']


