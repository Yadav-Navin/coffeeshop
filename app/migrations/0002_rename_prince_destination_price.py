# Generated by Django 4.2.5 on 2023-10-07 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='prince',
            new_name='price',
        ),
    ]
