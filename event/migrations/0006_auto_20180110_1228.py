# Generated by Django 2.0 on 2018-01-10 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20180110_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 12, 28, 22, 315671)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 12, 28, 22, 315671)),
        ),
    ]
