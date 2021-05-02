from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur", widget=forms.TextInput({"class": "form-control"}))
    password = forms.CharField(
        label="Mot de passe",  widget=forms.PasswordInput({"class": "form-control"}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur", widget=forms.TextInput({"class": "form-control"}))
    first_name = forms.CharField(
        label="Prénom", widget=forms.TextInput({"class": "form-control"}))
    last_name = forms.CharField(
        label="Nom de famille", widget=forms.TextInput({"class": "form-control"}))
    password1 = forms.CharField(
        label="Mot de passe",  widget=forms.PasswordInput({"class": "form-control"}))
    password2 = forms.CharField(
        label="Confirmation Mot de passe",  widget=forms.PasswordInput({"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "first_name",
                  "last_name", "password1", "password2"]
