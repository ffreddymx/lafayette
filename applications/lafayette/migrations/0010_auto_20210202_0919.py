# Generated by Django 3.1.5 on 2021-02-02 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lafayette', '0009_amigo_finalizada'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='amigo',
            name='cliente',
            field=models.CharField(max_length=60, verbose_name='Nombre Completo del Cliente'),
        ),
    ]