# Generated by Django 3.1 on 2020-09-02 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200902_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 2, 17, 36, 28, 724890), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_slug',
            field=models.CharField(max_length=200),
        ),
    ]
