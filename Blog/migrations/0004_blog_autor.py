# Generated by Django 4.1.3 on 2023-01-10 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_blog_director_alter_blog_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='autor',
            field=models.CharField(default='autor', max_length=100),
            preserve_default=False,
        ),
    ]
