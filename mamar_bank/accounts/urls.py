from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    userLogout,
    UserBankAccountUpdateView,
    CustomPasswordChangeView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", userLogout, name="logout"),
    path("profile/", UserBankAccountUpdateView.as_view(), name="profile"),
    path("passchange/", CustomPasswordChangeView.as_view(), name="passchange"),
]
