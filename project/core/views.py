from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'core/index.html')


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')
