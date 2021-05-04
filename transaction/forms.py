from product.models import Product
from django import forms
from .models import Transaction


class SpentForm(forms.ModelForm):
    quantity = forms.CharField(
        label="Quantite depensée", widget=forms.NumberInput({"class": "form-control"}))
    price = forms.CharField(
        label="Prix", widget=forms.NumberInput({"class": "form-control"}))

    class Meta:
        model = Transaction
        fields = ("quantity", "price",)


class IncomeForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(), widget=forms.Select({"class": "form-control"}))
    quantity = forms.CharField(
        label="Quantite vendu", widget=forms.NumberInput({"class": "form-control"}))
    price = forms.CharField(
        label="Prix", widget=forms.NumberInput({"class": "form-control"}))

    class Meta:
        model = Transaction
        fields = ("product", "quantity", "price", )
