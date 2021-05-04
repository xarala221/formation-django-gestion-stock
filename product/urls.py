from django.urls import path
from .views import index, product_list, add_product, product_detail, edit_product, delete_product, AboutView

urlpatterns = [
    path("", index, name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("products/", product_list, name="product_list"),
    path("products/add/", add_product, name="add_product"),
    path("products/<int:product_id>/", product_detail, name="product_detail"),
    path("products/<int:product_id>/edit/", edit_product, name="edit_product"),
    path("products/<int:product_id>/delete/",
         delete_product, name="delete_product"),
]
