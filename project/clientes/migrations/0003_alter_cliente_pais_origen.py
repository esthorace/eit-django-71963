# Generated by Django 5.1 on 2024-09-07 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='pais_origen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.pais'),
        ),
    ]
