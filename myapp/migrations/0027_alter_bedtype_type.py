# Generated by Django 5.0.2 on 2024-04-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_blog_status_alter_blog_image_alter_hostel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedtype',
            name='type',
            field=models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Tripple', 'Tripple'), ('Four', 'Four')], max_length=50, unique=True),
        ),
    ]