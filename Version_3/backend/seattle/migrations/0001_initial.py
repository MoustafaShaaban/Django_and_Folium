# Generated by Django 4.1.3 on 2022-11-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'Hospital',
                'verbose_name_plural': 'Hospitals',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'Library',
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
    ]
