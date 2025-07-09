from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
class ProductCategorySerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(many=True, read_only=True, source='products')
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='User.name')
    categoy_id = ProductCategorySerializer(read_only=True, source='product.category')
    items_id = OrderItemSerializer(many=True, read_only=True, source='items')
    customer_id  = CustomerSerializer(read_only=True, source='customer')
    
    class Meta:
        model = Order
        fields = '__all__'