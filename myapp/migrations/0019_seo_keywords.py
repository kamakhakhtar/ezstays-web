# Generated by Django 5.0.2 on 2024-04-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_remove_seo_keywords_alter_seo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='keywords',
            field=models.TextField(null=True),
        ),
    ]
