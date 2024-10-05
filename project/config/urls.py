from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from config import settings

from . import views

# path('saludar/', views.saludar),
# path('saludar-con-etiqueta', views.saludar_con_etiqueta),
# path('saludar-con-parametros/<str:nombre>/<str:apellido>', views.saludar_con_parametros),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('productos/', include('productos.urls', namespace='productos')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
