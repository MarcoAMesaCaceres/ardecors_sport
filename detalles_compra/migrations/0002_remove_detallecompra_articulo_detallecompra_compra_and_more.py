# Generated by Django 4.2.9 on 2024-08-12 22:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_compras_producto_alter_compras_id'),
        ('detalles_compra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecompra',
            name='articulo',
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='compra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='compras.compras'),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='producto',
            field=models.CharField(default='Producto Desconocido', max_length=255),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
