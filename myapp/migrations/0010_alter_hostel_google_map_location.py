# Generated by Django 5.0.2 on 2024-04-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_hostel_cafeteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='google_map_location',
            field=models.URLField(max_length=2000),
        ),
    ]