from django.contrib import admin

from .models import Producto, ProductoCategoria

admin.site.register(ProductoCategoria)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre', 'stock', 'unidad_medida', 'precio')
    list_filter = ('categoria', 'unidad_medida')
    search_fields = ('nombre', 'categoria__nombre')
