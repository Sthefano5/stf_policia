# Generated by Django 5.0.2 on 2024-02-13 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_alter_mantenimiento_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='personamodel',
            name='cedula',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
