from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required

from .forms import UserAdminCreationForm
from .models import User



# Create your views here.

class IndexView(TemplateView):
    template_name = 'accounts/index.html'

index = login_required(IndexView.as_view())


class login(TemplateView):
    template_name = 'accounts/accounts/login.html'


class RegisterView(CreateView):
    model = User
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'





