from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView

from .forms import UserAdminCreationForm
from .models import User



# Create your views here.


class login(TemplateView):
    template_name = 'accounts/login.html'


class RegisterView(CreateView):
    model = User
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'





