# Generated by Django 4.2.13 on 2024-07-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('contraseña', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('rut', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=45)),
            ],
        ),
    ]
