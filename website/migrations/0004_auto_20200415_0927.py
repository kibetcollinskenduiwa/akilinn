# Generated by Django 3.0.5 on 2020-04-15 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200415_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Image',
            field=models.ImageField(default=django.utils.timezone.now, height_field=130, upload_to='home', width_field=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='Image',
            field=models.ImageField(default=django.utils.timezone.now, height_field=130, upload_to='home', width_field=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='Image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='projects'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subsidiaries',
            name='Image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='projects'),
            preserve_default=False,
        ),
    ]
