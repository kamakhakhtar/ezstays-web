# Generated by Django 5.0.2 on 2024-04-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_hostel_cafeteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='cafeteria',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=50),
        ),
    ]