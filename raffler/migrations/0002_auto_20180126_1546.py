# Generated by Django 2.0 on 2018-01-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raffler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raffler',
            name='draw_duration',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='raffler',
            name='item_duration',
            field=models.FloatField(default=1),
        ),
    ]
