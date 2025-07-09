from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at', 'created_by')
    search_fields = ('name','price', 'created_by')
    list_filter = ('created_at','created_by','updated_at')
    
    
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'created_at', 'updated_at')
    search_fields = ('customer__name',)
    list_filter = ('created_at', 'updated_at')
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'total')
    
class CutomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'phone')
    list_filter = ('created_at', 'updated_at')
    
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CutomerAdmin)
admin.site.register(OrderItem, OrderItemAdmin)