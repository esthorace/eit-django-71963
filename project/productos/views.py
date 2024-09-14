from django.shortcuts import render

from .forms import ProductoCategoriaForm
from .models import ProductoCategoria


def index(request):
    return render(request, 'productos/index.html')


def productocategoria_list(request):
    query = ProductoCategoria.objects.all()
    context = {'object_list': query}
    return render(request, 'productos/productocategoria_list.html', context)


def productocategoria_create(request):
    form = ProductoCategoriaForm()
    context = {'form': form}
    return render(request, 'productos/productocategoria_create.html', context)
