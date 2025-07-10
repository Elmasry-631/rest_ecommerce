from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # ← دي لازم تكون الكلاس نفسه، مش حقل منه
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
        )

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = (
            "user",
            "phone",
            "address",
            "profile_picture",
            "created_at",
            "updated_at",
        )
        