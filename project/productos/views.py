from django.shortcuts import redirect, render

from .forms import ProductoCategoriaForm
from .models import ProductoCategoria


def index(request):
    return render(request, 'productos/index.html')


def productocategoria_list(request):
    q = request.GET.get('q')
    if q:
        query = ProductoCategoria.objects.filter(nombre__icontains=q)
    else:
        query = ProductoCategoria.objects.all()
    context = {'object_list': query}
    return render(request, 'productos/productocategoria_list.html', context)


def productocategoria_create(request):
    if request.method == 'GET':
        form = ProductoCategoriaForm()

    if request.method == 'POST':
        form = ProductoCategoriaForm(request.POST)
        if form.is_valid():
            # nombre = form.cleaned_data['nombre'].capitalize()
            form.save()
            return redirect('productos:productocategoria_list')

    return render(request, 'productos/productocategoria_create.html', {'form': form})
