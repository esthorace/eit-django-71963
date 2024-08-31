from django.http import HttpResponse


def saludar(request):
    return HttpResponse('¡Hola Django!🔥')


def saludar_con_etiqueta(request):
    return HttpResponse('<h1 style="color: red;">¡Hola Django!🔥</h1>')


def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse(f'{apellido}, {nombre}')
