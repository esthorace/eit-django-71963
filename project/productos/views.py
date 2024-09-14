from django.shortcuts import render

from .models import ProductoCategoria


def index(request):
    return render(request, 'productos/index.html')


def productocategoria_list(request):
    query = ProductoCategoria.objects.all()
    context = {'object_list': query}
    return render(request, 'productos/productocategoria_list.html', context)
