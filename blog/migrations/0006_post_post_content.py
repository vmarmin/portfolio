# Generated by Django 3.1.1 on 2020-10-02 23:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201001_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
