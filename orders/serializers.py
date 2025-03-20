from rest_framework import serializers
from .models import Order
from restaurants.models import MenuItem

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), many=True)

    class Meta:
        model = Order
        fields = '__all__'
