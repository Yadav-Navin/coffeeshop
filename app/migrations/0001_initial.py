# Generated by Django 4.2.5 on 2023-10-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prince', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
