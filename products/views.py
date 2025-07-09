from .models import Product, ProductCategory, Order, OrderItem, Customer
from .serializers import ProductSerializer ,ProductCategorySerializer , OrderSerializer, CustomerSerializer, OrderItemSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status




class CustomPagination(PageNumberPagination):
    page_size = 3
class ProductsListView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    pagination_class = CustomPagination
    try:
        queryset = Product.objects.all()
    except :
        raise Response(detail="No products found", code=status.HTTP_404_NOT_FOUND)
    
class ProductCategoryListView(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
class OrderListView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    
    
class CustomerListView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class OrderItemListView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer