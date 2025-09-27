from rest_framework import serializers
from .models import Order, Item
from django.contrib.auth.models import User
from home.models import Product

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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = ["id","name","price"]

class OrderSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True)
    customer = serializers.StringRelatedField()

    class Meta:
        model = Orderfields = ["order_id","customer","items","total_price","created_at"]




