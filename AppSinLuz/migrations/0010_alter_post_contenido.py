# Generated by Django 3.2.8 on 2022-02-05 15:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSinLuz', '0009_remove_post_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]