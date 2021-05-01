from django.db import models
from product.models import Product


class Transaction(models.Model):
    SPENT = 0
    INCOME = 1

    TRANSACTION_TYPE_CHOICES = [
        (SPENT, "Dépense"),
        (INCOME, "Revenu")
    ]

    transaction_type = models.CharField(
        max_length=1, choices=TRANSACTION_TYPE_CHOICES, default=SPENT)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=13, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Produit: {self.product} {self.price * self.quantity}"
