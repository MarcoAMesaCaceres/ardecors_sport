# Generated by Django 5.0.7 on 2024-09-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("compras", "0003_compras_producto_alter_compras_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="compras",
            name="total",
        ),
        migrations.AlterField(
            model_name="compras",
            name="producto",
            field=models.CharField(max_length=255),
        ),
    ]
