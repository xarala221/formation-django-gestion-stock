from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="product/")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=13, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
