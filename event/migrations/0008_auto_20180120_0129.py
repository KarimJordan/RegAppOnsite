# Generated by Django 2.0 on 2018-01-19 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20180110_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 20, 1, 29, 43, 758058)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 20, 1, 29, 43, 758058)),
        ),
    ]
