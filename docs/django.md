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
