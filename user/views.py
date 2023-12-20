from rest_framework import generics

from .models import User
from .serializers import UserSerializer, UserLoginSerializer


class UserRegister(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserLogin(generics.RetrieveAPIView):
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()