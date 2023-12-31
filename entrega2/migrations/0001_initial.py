# Generated by Django 4.2.7 on 2023-11-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_emp', models.PositiveIntegerField(unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('puesto', models.CharField(choices=[('1', 'ADMINISTRADOR'), ('2', 'CAJERO'), ('3', 'MOSTRADOR')], max_length=15)),
                ('horario', models.CharField(choices=[('1', 'MATUTINO'), ('2', 'VESPERTINO')], max_length=10)),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('telefono', models.CharField(max_length=10, unique=True)),
                ('correo', models.CharField(max_length=30, unique=True)),
                ('contrasena', models.CharField(max_length=30)),
                ('habilitado', models.BooleanField(default=True)),
            ],
        ),
    ]
