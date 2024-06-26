# Generated by Django 4.2.5 on 2023-11-14 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0006_alter_miembro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='imagen',
            field=models.ImageField(null=True, upload_to='actividades/imagenes/'),
        ),
        migrations.AlterField(
            model_name='culto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='cultos/imagenes/'),
        ),
        migrations.AlterField(
            model_name='las_escuela_dominical',
            name='imagen',
            field=models.ImageField(null=True, upload_to='escuela_dominical/imagenes/'),
        ),
        migrations.AlterField(
            model_name='las_sociedade',
            name='imagen',
            field=models.ImageField(null=True, upload_to='sociedades/imagenes/'),
        ),
        migrations.AlterField(
            model_name='los_ministerio',
            name='imagen',
            field=models.ImageField(null=True, upload_to='ministerios/imagenes/'),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='Correo_Electronico',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='Direccion_Residencia',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='Escuela_Dominical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miembros.escuela_dominical'),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='Numero_Cedula',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='Numero_Celular',
            field=models.CharField(max_length=12),
        ),
    ]
