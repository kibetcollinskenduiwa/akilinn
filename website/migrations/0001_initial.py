# Generated by Django 3.0.5 on 2020-04-14 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=145)),
                ('About', models.CharField(blank=True, max_length=145)),
            ],
            options={
                'verbose_name': 'Specialization  Section',
                'db_table': 'About',
            },
        ),
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Body', models.TextField()),
            ],
            options={
                'verbose_name': 'Body section',
                'db_table': 'Careers',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(blank=True, max_length=45)),
                ('Post_Box', models.CharField(blank=True, max_length=45)),
                ('Fax', models.CharField(blank=True, max_length=45)),
                ('Facebook', models.CharField(blank=True, max_length=145)),
                ('Twitter', models.CharField(blank=True, max_length=145)),
                ('Instagram', models.CharField(blank=True, max_length=145)),
                ('LinkedIn', models.CharField(blank=True, max_length=145)),
                ('Address', models.TextField()),
            ],
            options={
                'verbose_name': 'Footer Section',
                'db_table': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Home page',
                'db_table': 'Home',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Project',
                'db_table': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Subsidiaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Subsidiaries',
                'db_table': 'Subsidiaries',
            },
        ),
    ]
