# Generated by Django 4.2.1 on 2023-06-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name: ')),
                ('address', models.CharField(max_length=100, verbose_name='Address: ')),
                ('level', models.IntegerField(max_length=2, verbose_name='Level: ')),
                ('image', models.ImageField(upload_to='images')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
