from django.urls import path
from user_account.views import RegisterAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'user_account'

urlpatterns = [
    path('users/', RegisterAPIView.as_view(), name='user_list_create'),

    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]