from django.db import models
from users.models import User
from restaurants.models import MenuItem

class Order(models.Model):
    STATUS_CHOICES = (
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Preparing')
    ordered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Order #{self.user.email}"
