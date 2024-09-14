from django.db import models


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    decripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'
