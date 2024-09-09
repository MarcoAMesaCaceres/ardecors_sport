# Generated by Django 5.0.7 on 2024-08-13 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("detalles_venta", "0002_alter_detalleventa_id"),
        ("ventas", "0003_alter_venta_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="detalleventa",
            name="venta",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="detalles",
                to="ventas.venta",
            ),
        ),
    ]
