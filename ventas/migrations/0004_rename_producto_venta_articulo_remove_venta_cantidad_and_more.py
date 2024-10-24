# Generated by Django 5.0.7 on 2024-08-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ventas", "0003_alter_venta_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="venta",
            old_name="producto",
            new_name="articulo",
        ),
        migrations.RemoveField(
            model_name="venta",
            name="cantidad",
        ),
        migrations.RemoveField(
            model_name="venta",
            name="precio_unitario",
        ),
        migrations.AlterField(
            model_name="venta",
            name="cliente",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="venta",
            name="fecha",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="venta",
            name="total",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
