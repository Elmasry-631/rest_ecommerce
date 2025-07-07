from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at', 'created_by')
    search_fields = ('name','price', 'created_by')
    list_filter = ('created_at','created_by','updated_at')
    
admin.site.register(Product, ProductAdmin)