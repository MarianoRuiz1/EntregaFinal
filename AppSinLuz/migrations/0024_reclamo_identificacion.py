# Generated by Django 4.0 on 2022-02-10 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSinLuz', '0023_reclamo_problema_reclamo_resumen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='identificacion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
