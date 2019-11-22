from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='RegisterView'),
    path('accounts', include('django.contrib.auth.urls')),
    path('alterar-dados', views.update_user, name='update_user'),
    path('alterar-senha', views.update_password, name='update_password'),
    path('', views.index, name='MinhaConta'),

]