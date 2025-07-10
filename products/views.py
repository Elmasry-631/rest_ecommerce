from .models import Product, ProductCategory, Order, OrderItem, Customer
from .serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    OrderSerializer,
    CustomerSerializer,
    OrderItemSerializer,
)
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CustomPagination(PageNumberPagination):
    page_size = 3


class ProductsListView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = "slug"
    pagination_class = CustomPagination
    try:
        queryset = Product.objects.all()
    except Exception:
        queryset = Product.objects.none()


class ProductCategoryListView(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class OrderListView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CustomerListView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderItemListView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderGenericListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
