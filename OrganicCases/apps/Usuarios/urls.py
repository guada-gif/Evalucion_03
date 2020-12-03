from django.urls import path, include
from . import views
from .views import RegistroUsuario
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),

]
