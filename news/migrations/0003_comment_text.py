# Generated by Django 4.0.6 on 2022-08-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_name_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.CharField(default='Comment: ', max_length=500),
        ),
    ]
