from django.shortcuts import render
from rest_framework import status,generics,permissions

from rest_framework.response import Response
from user_account.models import User
from user_account.serializers import UserSerializer,UserListSerializer
from user_account.paginations import UserListPagination
# Create your views here.
class RegisterAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    pagination_class = UserListPagination
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserSerializer
        return UserListSerializer