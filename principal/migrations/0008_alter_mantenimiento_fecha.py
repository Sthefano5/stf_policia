# Generated by Django 5.0.2 on 2024-02-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_tipomantenimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimiento',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
