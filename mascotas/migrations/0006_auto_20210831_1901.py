# Generated by Django 3.2.6 on 2021-08-31 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0005_alter_cliente_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratarplan',
            name='nombreCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.cliente'),
        ),
        migrations.AlterField(
            model_name='contratarplan',
            name='nombreMascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.mascota'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.cliente'),
        ),
    ]
