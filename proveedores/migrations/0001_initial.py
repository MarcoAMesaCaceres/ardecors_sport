# Generated by Django 5.0.7 on 2024-08-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=255)),
                ("contacto", models.CharField(blank=True, max_length=255, null=True)),
                ("telefono", models.CharField(blank=True, max_length=20, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("direccion", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
