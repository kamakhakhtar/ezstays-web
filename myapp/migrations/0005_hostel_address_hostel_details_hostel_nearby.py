# Generated by Django 5.0.2 on 2024-04-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_hostel_bath_hostel_bed_hostel_cafeteria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hostel',
            name='details',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hostel',
            name='nearby',
            field=models.CharField(default='Sharda University : 0.2km', max_length=255),
        ),
    ]
