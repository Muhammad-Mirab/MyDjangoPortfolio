# Generated by Django 3.2.16 on 2023-07-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0012_alter_whatido_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebarinfo',
            name='buyMeACoffeeLink',
            field=models.CharField(blank=True, default='#', max_length=100, null=True),
        ),
    ]
