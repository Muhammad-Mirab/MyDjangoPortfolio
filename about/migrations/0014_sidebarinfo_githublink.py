# Generated by Django 3.2.16 on 2023-07-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_sidebarinfo_buymeacoffeelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebarinfo',
            name='githubLink',
            field=models.CharField(blank=True, default='#', max_length=100, null=True),
        ),
    ]
