from django.urls import path
from .views import index, product_list

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list, name="product_list")
]
