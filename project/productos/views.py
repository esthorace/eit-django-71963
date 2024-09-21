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

    return render(request, 'productos/productocategoria_form.html', {'form': form})


def productocategoria_detail(request, pk: int):
    query = ProductoCategoria.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'productos/productocategoria_detail.html', context)


def productocategoria_update(request, pk: int):
    query = ProductoCategoria.objects.get(id=pk)
    if request.method == 'GET':
        form = ProductoCategoriaForm(instance=query)

    if request.method == 'POST':
        form = ProductoCategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('productos:productocategoria_list')

    return render(request, 'productos/productocategoria_form.html', {'form': form})


def productocategoria_delete(request, pk: int):
    query = ProductoCategoria.objects.get(id=pk)
    context = {'object': query}
    if request.method == 'POST':
        query.delete()
        return redirect('productos:productocategoria_list')
    return render(request, 'productos/productocategoria_confirm_delete.html', context)
