# Generated by Django 4.0 on 2022-02-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSinLuz', '0018_rename_descripcion_reclamo_detalles'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='usuario',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
