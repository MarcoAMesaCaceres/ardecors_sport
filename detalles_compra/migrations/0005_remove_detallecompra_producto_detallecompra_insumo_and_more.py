# Generated by Django 4.2.9 on 2024-09-27 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insumos', '0001_initial'),
        ('detalles_compra', '0004_remove_detallecompra_fecha_detallecompra_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecompra',
            name='producto',
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='insumo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insumos.insumos'),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]
