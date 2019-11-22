from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, CreateView, UpdateView, FormView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

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


class UpdateUserView(UpdateView):
    model = User
    template_name = 'accounts/alterar-dados.html'
    # Em fields podemos escolher os campos que o usuario vai poder alterar.
    fields = ['name', 'email']
    success_url = reverse_lazy('MinhaConta')

    # Iremos sobrescrever a função get_object para que retorne o usuário logado.
    def get_object(self):
        return self.request.user

update_user = login_required(UpdateUserView.as_view())


class UpdatePasswordView(FormView):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('MinhaConta')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


update_password = login_required(UpdatePasswordView.as_view())


