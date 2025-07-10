from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = "accounts"

router.register(r"users", views.UserViewSet, basename="user")

router.register(r"profiles", views.ProfileViewSet, basename="profile")


urlpatterns = [
    path("", include(router.urls)),
]
