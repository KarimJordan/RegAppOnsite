# Generated by Django 2.0 on 2018-01-02 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20180102_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 2, 18, 30, 44, 420982)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 2, 18, 30, 44, 420982)),
        ),
    ]