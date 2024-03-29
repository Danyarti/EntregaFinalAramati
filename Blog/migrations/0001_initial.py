# Generated by Django 4.1.3 on 2023-01-07 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('pais_origen', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to=None)),
            ],
        ),
    ]
