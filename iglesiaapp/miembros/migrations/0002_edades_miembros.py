# Generated by Django 4.2.5 on 2023-11-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edades',
            name='miembros',
            field=models.ManyToManyField(related_name='edades', to='miembros.miembro'),
        ),
    ]
