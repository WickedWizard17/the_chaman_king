# Generated by Django 4.2.7 on 2023-11-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_remove_empleado_turno_alter_empleado_sueldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
