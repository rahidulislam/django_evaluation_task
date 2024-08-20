from django.urls import path
from user_account.views import RegisterAPIView

app_name = 'user_account'

urlpatterns = [
    path('users/', RegisterAPIView.as_view(), name='user_list_create'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
]