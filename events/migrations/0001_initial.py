# Generated by Django 4.2.2 on 2023-07-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('MUSIC', 'Music'), ('SPORTS', 'Sports'), ('SCIENCE', 'Science'), ('TECHNOLOGY', 'Technology')], default='FREE', max_length=50)),
                ('event_access', models.CharField(choices=[('FREE', 'Free'), ('PAID', 'Paid')], default='FREE', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('MUSIC', 'Music'), ('SPORTS', 'Sports'), ('SCIENCE', 'Science'), ('TECHNOLOGY', 'Technology')], default='FREE', max_length=50)),
                ('event_access', models.CharField(choices=[('FREE', 'Free'), ('PAID', 'Paid')], default='FREE', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('event', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('speaker_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('linkedin_link', models.URLField()),
                ('twitter_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SpeakerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('linkedin_link', models.URLField()),
                ('twitter_link', models.URLField()),
            ],
        ),
    ]
