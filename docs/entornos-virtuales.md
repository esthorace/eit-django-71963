# Entorno virtuales

## Instalación de uv

Usaremos `uv`, que es un moderno rápido administrador de proyectos para Python, escrito en Rust. Ver la página oficial: <https://docs.astral.sh/uv/>

Instalación para Windows:

    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

Instalación para macOs y Linux:

    curl -LsSf https://astral.sh/uv/install.sh | sh

Luego de la instalación, reiniciar toda terminal.

Para actualizar `uv` (cuando ya lo hayamos instalado) ejecutar en la terminal:

    uv self update

## Sincronización de un proyecto Python

Si tenemos en algún proyecto el archivo `pyproject.toml` que tiene las dependencias que necesitamos para el desarrollo, por ejemplo: `django` y `pillow`, y otras  herramientas para el desarrollo, que no son propias del proyecto, como por ejemplo: `ruff`, `djlint` y `ipython`, entonces, sólo necesitamos sincronizar el proyecto con el siguiente comando:

    uv sync

Automáticamente se creará el entorno virtual y agregará las dependencias ya predefinidas. Restará activar el entorno.

## Creación de un proyecto desde 0 con `uv`

Una vez `uv` instalado y actualizado, crear una carpeta con el nombre del proyecto, vacía, acceder a ella, y ejecutar:

    uv init

Esto creará algunos archivos. Nunca deberemos eliminar `pyproject.toml` y `uv.lock`. Podemos probar ejecutando:

    python hello.py

Ya podemos borrar `hello.py`

Luego creamos el entorno virtual:

    uv venv

## Activación del entorno virtual

Si usas Windows, por única vez debes darle permiso para la ejecución de scripts, y así activar el entorno virtual. Entonces, abrir `Microsoft PowerShell` en modo *administrador*, y ejecutar el comando:

    Set-ExecutionPolicy Unrestricted

Luego cerrar todas las terminales abiertas para que los cambios tengan efecto.

Una vez que se haya creado la carpeta `.venv` gracias al comando `uv venv` (si el proyecto no tiene el archivo pyproject.toml) o `uv sync` (si el proyecto sí tiene el archivo `pyproject.toml`), entonces, debemos activarlo, para luego agregar las dependencias que usaremos en el proyecto:

Usuarios de Windows:

    .venv\Scripts\activate

Usuarios de Linux o Mac:

    source .venv/bin/activate

## Instalación de dependencias

Ahora agregaremos los paquetes que usaremos en el proyecto:

    uv add django
    uv add pillow

Y los paquetes que servirán de herramienta para el desarrollo:

    uv add ruff --dev
    uv add djlint --dev
    uv add ipython --dev

Finalmente podemos ver la estructura de los paquetes:

    uv tree

Si queremos borrar un paquete, podemos usar:

    uv remove djlint --dev

o

    uv remove pillow

Hemos visto una herramiento superior a `pip` y otros administradores, por su velocidad y simplicidad. Ver la documentación oficial de `uv` para más información.
