# Generated by Django 5.0.2 on 2024-02-23 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0020_registrocombustible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrocombustible',
            name='fecha_hora',
        ),
    ]