# Generated by Django 2.0 on 2018-01-10 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0003_auto_20180110_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestinfofield',
            name='guest_id',
        ),
        migrations.RemoveField(
            model_name='guestinfofield',
            name='value',
        ),
    ]
