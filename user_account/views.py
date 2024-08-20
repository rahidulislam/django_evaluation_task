from django.shortcuts import render
from rest_framework import status,generics,permissions
from rest_framework.response import Response
from user_account.models import User
from user_account.serializers import UserSerializer
# Create your views here.
class RegisterAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]