# Generated by Django 2.0 on 2018-01-10 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0004_auto_20180110_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestinfo',
            name='guest_info_field_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guest.GuestInfoField'),
        ),
    ]