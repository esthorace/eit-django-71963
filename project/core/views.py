from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomProfileForm, CustomUserCreationForm


def index(request):
    return render(request, 'core/index.html')


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')


class ProfileView(UpdateView):
    model = get_user_model()
    form_class = CustomProfileForm
    template_name = 'core/profile.html'
    success_url = reverse_lazy('core:index')

    def get_object(self):
        # Devuelve el usuario actual en lugar de devolver el pk
        return self.request.user
