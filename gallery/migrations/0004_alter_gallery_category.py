# Generated by Django 3.2.16 on 2023-07-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_gallery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Landscapes', 'Landscapes')], default='General', max_length=256),
        ),
    ]
