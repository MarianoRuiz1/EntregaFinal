# Generated by Django 4.0 on 2022-02-10 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSinLuz', '0020_reclamo_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamo',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='reclamo',
            name='usuario',
        ),
    ]