# Generated by Django 3.1.5 on 2021-01-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lafayette', '0003_auto_20210127_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='publicar',
            field=models.CharField(choices=[('1', 'Publicar'), ('2', 'Privado')], default=2, max_length=20, verbose_name='Esta nota sera ?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amigo',
            name='opcion',
            field=models.CharField(choices=[('1', 'Publicar'), ('2', 'Privado')], max_length=20, verbose_name='Operacion a realizar'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='datos',
            field=models.CharField(max_length=600, verbose_name='Datos de la propiedad'),
        ),
    ]
