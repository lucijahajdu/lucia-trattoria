# Generated by Django 3.2.21 on 2023-09-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('guests', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('requirements', models.CharField(max_length=200)),
                ('user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('requirements', models.CharField(max_length=200)),
                ('user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
    ]