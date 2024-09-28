from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('register', views.CustomRegisterView.as_view(), name='register'),
    path('profile', views.ProfileView.as_view(), name='profile'),
]
