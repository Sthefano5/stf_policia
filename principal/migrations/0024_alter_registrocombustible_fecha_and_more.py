# Generated by Django 5.0.2 on 2024-02-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0023_registrocombustible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocombustible',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='registrocombustible',
            name='fecha_solicitud',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='registrocombustible',
            name='hora',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
