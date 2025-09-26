from django.shortcuts import render
from rest_framework.respones import respones
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import order.MenuItem
from .serializers import OrderSerializer,MenuItemSerializer
from django.http import JsonResponse
from utils.validation_utils import is_valid_email
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination


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

class UpdateMenuItem(APIView):
    def put(self, request, pk):
        item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuItemSearchView(ListAPIView):
    serializer_class = MenuItemSerializer
    pagination_class = PageNumberPagination

    def get_queryset(Self):
        query = self.request.query_params.get('q',None)
        queryset = MenuItem.objects.all()
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

class UserProfileViewSet(Viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['put'])
    def update_profile(self, request):
        user = request.userserializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Profile updated succesfully", "data":serializer.data})
        return Response(serializer.errors, status=400)

def PLACE_ORDER(request):
    order_id =1234
    customer_email = "patildevesh677@gmail.com"
    customer_name = "devesh patil"

    result =send_order_confirmation_email(order_id, customer_email, customer_name)
    return JsonResponse(result)



