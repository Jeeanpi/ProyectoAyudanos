# Generated by Django 3.2.6 on 2021-09-03 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0006_auto_20210831_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
