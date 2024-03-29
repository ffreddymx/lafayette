# Generated by Django 3.1.5 on 2021-01-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210128_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nivel',
            field=models.CharField(blank=True, choices=[('JR', 'JR'), ('PLATA', 'PLATA'), ('ORO', 'ORO'), ('PREMIER', 'PREMIER')], max_length=7),
        ),
        migrations.AddField(
            model_name='user',
            name='ventas',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='apellidos',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='estado',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='municipio',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombres',
            field=models.CharField(max_length=30),
        ),
    ]
