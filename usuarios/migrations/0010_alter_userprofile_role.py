# Generated by Django 4.2.9 on 2024-10-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_userprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('superuser', 'Superusuario'), ('admin', 'Admin'), ('employee', 'Empleado')], default='employee', max_length=10),
        ),
    ]
