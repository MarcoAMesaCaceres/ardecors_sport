# Generated by Django 4.2.9 on 2024-10-09 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_alter_compras_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]