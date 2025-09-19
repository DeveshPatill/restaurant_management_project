from django.shortcuts import render
from rest_framework.respones import respones
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import order.MenuItem
from .serializers import OrderSerializer,MenuItemSerializer
from django.http import JsonResponse
from utils.validation_utils import is_valid_email


# Create your views here.
class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        orders = order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return respone(serializer)

@api_view(['GET'])
def menu_items_by_category(request):
    category = request.query_params.get('category')
    if category:
        items = MenuItem.objects.filter(category__name__iexact=category)
    else:
        items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)

def submit_email(request):
    email = request.GET.get("email")
    if not email:
        return JsonResponse({"error":"Email is required"}, status=400)
    if is_valid_email(email):
        return JsonResponse({"message":"valid email address"})
    else:
        return JsonResponse({"error":"Invalid Email address"},status=400)



