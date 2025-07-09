from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
router = DefaultRouter()
router.register(r'products', ProductsListView, basename='product')
router.register(r'product-categories', ProductCategoryListView, basename='product-category')
router.register(r'orders', OrderListView, basename='order')
# router.register(r'items', OrderItemListView, basename='order-item')
router.register(r'customers', CustomerListView, basename='customer')


urlpatterns = [
    path('', include(router.urls)),
    # path('products/', ProductsListView.as_view(), name='products-list'),
    # path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    # path('products/create/', ProductCreateView.as_view(), name='product-create'),
    # path('products/<slug:slug>/update/', ProductUpdateView.as_view(), name='product-update'),
    # path('products/<slug:slug>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]