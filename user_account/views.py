from django.shortcuts import get_object_or_404
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from user_account.models import User
from user_account.serializers import (
    UserListSerializer,
    UserRegisterSerializer,
    UserDetailUpdateSerializer,
)
from user_account.paginations import UserListPagination


# Create your views here.
class RegisterAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    pagination_class = UserListPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserListSerializer


class UserDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "patch", "delete"]

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get("pk"))

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if request.user == user:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user.is_superuser or request.user == user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"detail": "you are not allowed to delete this user"},
            status=status.HTTP_400_BAD_REQUEST,
        )
