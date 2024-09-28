from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Vendedor)


@admin.register(models.Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'producto', 'cantidad', 'precio_total', 'fecha_venta')
    list_filter = ('vendedor',)
    search_fields = ('vendedor__nombre', 'producto__nombre')
    date_hierarchy = 'fecha_venta'
    ordering = ('-fecha_venta',)
