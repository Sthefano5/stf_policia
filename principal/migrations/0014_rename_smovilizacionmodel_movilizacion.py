# Generated by Django 5.0.2 on 2024-02-18 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_rename_solicitudmovilizacion_smovilizacionmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SMovilizacionModel',
            new_name='movilizacion',
        ),
    ]
