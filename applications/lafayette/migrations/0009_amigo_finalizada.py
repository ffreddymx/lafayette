# Generated by Django 3.1.5 on 2021-01-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lafayette', '0008_amigo_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='finalizada',
            field=models.BooleanField(default=False),
        ),
    ]