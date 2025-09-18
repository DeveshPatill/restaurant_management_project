from django.shortcuts import render
from rest_framework.respones import respones
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import order
from .serializers import OrderSerializer


# Create your views here.
class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        orders = order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return respone(serializer)
