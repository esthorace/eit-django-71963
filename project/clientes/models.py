from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    dni = models.CharField(max_length=15, null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.apellido}, {self.nombre}'
