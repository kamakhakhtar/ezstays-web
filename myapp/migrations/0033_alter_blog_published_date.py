# Generated by Django 5.0.2 on 2024-05-20 06:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]