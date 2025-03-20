from rest_framework.permissions import BasePermission

class IsOwnerOrRestaurantOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True

        if request.user.role == "restaurant_owner":
            return obj.items.filter(restaurant__owner=request.user).exists()

        return False  # Otherwise, deny access
