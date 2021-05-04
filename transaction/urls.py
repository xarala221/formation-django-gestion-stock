from django.urls import path
from .views import add_spent, add_income, all_transactions

urlpatterns = [
    path("add-spent/", add_spent, name="add_spent",),
    path("add-income/", add_income, name="add_income",),
    path("list/", all_transactions, name="transaction_list"),
]
