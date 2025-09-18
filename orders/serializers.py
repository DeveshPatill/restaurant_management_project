from rest_framework import serializers
from .models import Order, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =Item
        fields = ["id", "name","price"]

class OrderSerializer(Serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model =Orderfields =["id","date","total_price","items"]