# Generated by Django 3.0.5 on 2020-04-15 08:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200414_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='Address',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
