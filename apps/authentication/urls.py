from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegistrationView

urlpatterns = [
    path("login/", obtain_auth_token, name="api_login"),
    path("logout/", LogoutView.as_view(), name="api_logout"),
    path("register/", RegistrationView.as_view(), name="registration"),
    path("token/", obtain_auth_token, name="token_obtain_pair"),
]
