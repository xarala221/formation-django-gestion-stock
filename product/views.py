from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product


@login_required
def index(request):
    return render(request, "index.html")


@login_required
def product_list(request):
    user = request.user
    products = Product.objects.filter(owner=user)
    return render(request, "product/product-list.html", {"products": products})
