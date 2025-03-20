from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegisterSerializer, UserSerializer, DepositSerializer
from django.contrib.auth import get_user_model
from . serializers import CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]


class DepositView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = DepositSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        user_id = kwargs['id']
        user = self.get_object()
        amount = request.data.get('amount')

        if amount <= 0:
            return Response({'error': 'Invalid deposit amount'}, status=status.HTTP_400_BAD_REQUEST)

        user.balance += amount
        user.save()

        return Response({'message': f'Deposited ${amount} into user {user_id} account'}, status=status.HTTP_200_OK)


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user