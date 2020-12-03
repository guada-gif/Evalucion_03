from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuarios/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')
