from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Vendedor(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='vendedor'
    )
    celular = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self) -> str:
        return self.usuario.username


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey('productos.Producto', on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['-fecha_venta']

    def clean(self):
        if self.cantidad > self.producto.stock:
            raise ValidationError('No hay suficiente stock para realizar la venta')

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)
