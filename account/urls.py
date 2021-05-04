from django.urls import path
from .views import login_user, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register_user, name="register")
]
