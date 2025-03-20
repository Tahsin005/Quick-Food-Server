from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOwnerOrRestaurantOwner
from users.models import User
from restaurants.models import MenuItem
from django.db import transaction
from rest_framework import serializers

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrRestaurantOwner]

    def get_queryset(self):
        user = self.request.user

        if user.role == "restaurant_owner":
            return Order.objects.filter(items__restaurant__owner=user).distinct()

        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        items = serializer.validated_data.get('items')

        item_ids = [item.id for item in items]

        total_cost = sum(MenuItem.objects.filter(id__in=item_ids).values_list('price', flat=True))

        with transaction.atomic():
            if user.balance < total_cost:
                raise serializers.ValidationError({
                    'balance': 'Insufficient balance to complete this order.'
                })

            serializer.save(user=user)
            user.balance -= total_cost
            user.save()

        return serializer.instance
