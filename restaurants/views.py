from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer
from .permissions import IsOwnerOrReadOnly, IsRestaurantOwnerOrReadOnly
from rest_framework.exceptions import PermissionDenied

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            return queryset.filter(
                name__icontains=query
            ) | queryset.filter(
                location__icontains=query
            )
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, IsRestaurantOwnerOrReadOnly]

    def perform_create(self, serializer):
        restaurant = serializer.validated_data.get("restaurant")
        if restaurant.owner != self.request.user:
            raise PermissionDenied("You do not have permission to add items to this restaurant.")
        serializer.save()
