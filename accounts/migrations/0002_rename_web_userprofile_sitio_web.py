# Generated by Django 5.2.3 on 2025-07-04 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='web',
            new_name='sitio_web',
        ),
    ]
