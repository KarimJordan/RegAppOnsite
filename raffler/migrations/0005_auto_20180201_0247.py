# Generated by Django 2.0 on 2018-01-31 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raffler', '0004_auto_20180131_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raffler',
            name='background_image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='raffler',
            name='prize_image',
            field=models.TextField(),
        ),
    ]