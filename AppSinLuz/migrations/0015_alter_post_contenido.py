# Generated by Django 3.2.8 on 2022-02-06 15:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSinLuz', '0014_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(max_length=140),
        ),
    ]