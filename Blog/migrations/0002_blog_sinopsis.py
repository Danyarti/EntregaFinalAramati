# Generated by Django 4.1.3 on 2023-01-08 23:01

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sinopsis',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='test'),
            preserve_default=False,
        ),
    ]
