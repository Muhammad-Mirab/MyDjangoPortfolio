# Generated by Django 3.2.16 on 2023-07-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityandeducation',
            name='endDate',
            field=models.DateTimeField(verbose_name='ending time(blank for still going)'),
        ),
        migrations.AlterField(
            model_name='universityandeducation',
            name='startDate',
            field=models.DateTimeField(verbose_name='starting time'),
        ),
    ]