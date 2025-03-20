from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView, DepositView, CurrentUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('users/<int:id>/deposit/', DepositView.as_view(), name='deposit'),
    path('users/me/', CurrentUserView.as_view(), name='current_user'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
