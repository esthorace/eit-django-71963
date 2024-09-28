from django.db import models


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'


class Producto(models.Model):
    """Productos corresponden a una categoría"""

    categoria = models.ForeignKey(
        ProductoCategoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='categoría',
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad_medida = models.CharField(max_length=50)
    stock = models.FloatField()
    fecha_actualizacion = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return f'{self.nombre} ({self.unidad_medida}) ${self.precio:.2f}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_actualizacion']
        # La siguiente línea es para que no se repitan los productos
        # unique_together = ('categoria', 'nombre')
        constraints = [
            models.UniqueConstraint(
                fields=['categoria', 'nombre'],
                name='unique_producto_categoria_nombre',
            )
        ]
        # Indexación
        indexes = [models.Index(fields=['nombre'])]
