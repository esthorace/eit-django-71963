# Django

## Creación de un proyecto

Creamos una carpeta del proyecto, con cualquier nombre y abrimos Visual Studio Code en esa carpeta.

Creamos una carpeta llamada 'project':

    mkdir project

Accedemos a ella:

    cd project

Instalamos la configuración de Django ahí

    django-admin startproject config .

Observemos el espacio y el punto del comando anterior. son importantes.

Probamos que el servidor de Django funcione:

    python manage.py runserver

Abrir en el navegador la ruta y el puerto que nos da Django:

    127.0.0.1:8000

En el navegador, veremos la bienvenida de Django.

## Creación de una aplicación

Creamos una aplicación llamada 'core':

    cd project
    python manage.py startapp core

Registrarla en `config.settings`

    INSTALLED_APPS = [
        ...
        'core',
    ]

## Crear un modelo

Creamos un modelo en `models`

Realizamos las migraciones:

    python manage.py makemigrations

Aplicamos las migraciones:

    python manage.py migrate

## Crear un superusuario

    python manage.py createsuperuser

## Registrar el modelo en el panel de administración

Modificamos `core.admin`:

    from django.contrib import admin
    from .models import Modelo
    admin.site.register(Modelo)

## Crear la plantilla

Creamos una carpeta `templates` en la aplicación. Y dentro de ella, una carpeta con el nombre de la aplicación. Es una buena práctica crear un archivo llamado `index.html` en esa carpeta.

Path absoluto:

    project/core/templates/core/index.html

## Crear una vista

Abrir el módulo `core.views`:

    from django.shortcuts import render
    def index(request):
        return render(request, 'core/index.html')

## Crear una URL

Crear el módulo `core.urls`:

    from django.urls import path
    from . import views

    app_name = 'core'

    urlpatterns = [
        path('', views.index, name='index'),
    ]

## Registrar la URL en el proyecto

Abrir el archivo `config.urls` del proyecto:

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('core.urls', namespace='core')),
        path('clientes/', include('clientes.urls', namespace='clientes')),
    ]
