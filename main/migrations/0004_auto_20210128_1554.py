# Generated by Django 3.1.4 on 2021-01-28 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210128_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorials',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 54, 14, 307965), verbose_name='date published'),
        ),
    ]
