# Generated by Django 2.2.12 on 2020-05-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datosuser',
            options={'verbose_name': 'Dato de usuario', 'verbose_name_plural': 'Datos de los usuarios'},
        ),
        migrations.AlterModelOptions(
            name='rates',
            options={'verbose_name': 'Nivel de habilidad', 'verbose_name_plural': 'Niveles de los usuarios'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'Perfil de usuario', 'verbose_name_plural': 'perfiles'},
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='direccion',
            field=models.CharField(max_length=255, verbose_name='Direccion de usuario'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='fotoUser',
            field=models.ImageField(default='user.png', upload_to='', verbose_name='Foto de perfil'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='upData',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
    ]
