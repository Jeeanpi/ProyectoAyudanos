# Generated by Django 3.2.6 on 2021-08-31 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_rename_nombre_contratarplan_nombrecliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='password',
            field=models.TextField(max_length=15),
        ),
    ]