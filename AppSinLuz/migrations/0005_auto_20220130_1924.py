# Generated by Django 3.2.8 on 2022-01-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSinLuz', '0004_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contrasena',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='password2',
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
