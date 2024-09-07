from django.contrib import admin

from .models import Cliente, Pais

admin.site.register(Pais)
admin.site.register(Cliente)
