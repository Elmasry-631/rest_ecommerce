from rest_framework.decorators import api_view
from accounts.serializer import UserSerializer
from accounts.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        data = UserSerializer(user).data
        return Response({'data': data})
    return Response({'error': 'Invalid credentials'}, status=401)


@api_view(['GET'])
def user_detail(request, id):
    user = User.objects.get(id=id)
    data = UserSerializer(user).data
    return Response({'data': data})