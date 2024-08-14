# Generated by Django 4.2.9 on 2024-08-13 18:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='nombre',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='El nombre solo puede contener letras y espacios.', regex='^[a-zA-Z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01, message='El precio debe ser un número positivo.')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='El stock debe ser un número positivo o cero.')]),
        ),
    ]