# Generated by Django 2.0 on 2018-01-18 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0005_guestinfo_guest_info_field_id'),
        ('layout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayoutField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('field_name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('with_placeholder', models.BooleanField(default=True)),
                ('font_family', models.CharField(max_length=200)),
                ('font_color', models.CharField(max_length=100)),
                ('font_size', models.IntegerField()),
                ('background_color', models.CharField(max_length=100)),
                ('opacity', models.IntegerField()),
                ('border_color', models.CharField(max_length=100)),
                ('label_color', models.CharField(max_length=100)),
                ('label_size', models.IntegerField()),
                ('page_num', models.IntegerField()),
                ('guest_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guest.GuestInfoField')),
                ('layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layout.Layout')),
            ],
        ),
        migrations.CreateModel(
            name='LayoutFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('layout_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layout.LayoutField')),
            ],
        ),
    ]
