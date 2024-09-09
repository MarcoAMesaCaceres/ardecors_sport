# Generated by Django 5.0.7 on 2024-08-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("descripcion", models.TextField(blank=True, null=True)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.IntegerField()),
            ],
        ),
    ]
