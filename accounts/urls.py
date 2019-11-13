from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='RegisterView'),
    path('', include('django.contrib.auth.urls')),

]