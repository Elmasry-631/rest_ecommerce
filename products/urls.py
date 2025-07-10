from django.urls import path, include
from .views import (
    OrderGenericListCreateView,
    ProductsListView,
    ProductCategoryListView,
    OrderListView,
    CustomerListView
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'products', ProductsListView, basename='product')
router.register(r'product-categories', ProductCategoryListView,
                basename='product-category')
router.register(r'orders', OrderListView, basename='order')
# router.register(r'items', OrderItemListView, basename='order-item')
router.register(r'customers', CustomerListView, basename='customer')


urlpatterns = [
    path('', include(router.urls)),

    path('generics/', OrderGenericListCreateView.as_view()),
    path('api-auth', include('rest_framework.urls'))
]
