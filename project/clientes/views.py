from django.shortcuts import render


def index(request):
    nombre = 'Louis'
    apellido = 'Van Beethoven'
    context = {
        'nombre': nombre,
        'apellido': apellido,
    }
    return render(request, 'clientes/index.html', context)


def notas(request):
    lista_de_notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        'notas': lista_de_notas,
    }
    return render(request, 'clientes/notas.html', context)
