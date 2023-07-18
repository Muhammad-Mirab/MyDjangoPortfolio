# Generated by Django 3.2.16 on 2023-07-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_whatido'),
    ]

    operations = [
        migrations.CreateModel(
            name='sideBarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('jobTitle', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('location', models.TextField(max_length=40)),
                ('linkedInLink', models.CharField(max_length=100)),
                ('twitterLink', models.CharField(max_length=100)),
                ('instagramLink', models.CharField(max_length=100)),
                ('telegramLink', models.CharField(max_length=100)),
            ],
        ),
    ]