# Generated by Django 3.2.16 on 2023-07-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_remove_sidebarinfo_youtubelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebarinfo',
            name='youtubeLink',
            field=models.CharField(blank=True, default='#', max_length=100, null=True),
        ),
    ]
