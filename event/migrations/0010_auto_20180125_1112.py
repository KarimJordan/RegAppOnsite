# Generated by Django 2.0 on 2018-01-25 03:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20180122_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 25, 11, 11, 13, 203119)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 25, 11, 11, 13, 203119)),
        ),
    ]