# Generated by Django 3.1.5 on 2021-01-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lafayette', '0007_auto_20210128_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='precio',
            field=models.FloatField(default=0, max_length=50, verbose_name='Precio '),
            preserve_default=False,
        ),
    ]
