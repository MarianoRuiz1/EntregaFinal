# Generated by Django 4.0 on 2022-02-07 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSinLuz', '0017_reclamo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reclamo',
            old_name='descripcion',
            new_name='detalles',
        ),
    ]