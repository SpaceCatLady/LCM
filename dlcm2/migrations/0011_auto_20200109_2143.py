# Generated by Django 3.0.1 on 2020-01-09 21:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dlcm2', '0010_auto_20200107_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinelog',
            name='med_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 9, 21, 43, 32, 648156, tzinfo=utc), verbose_name='Time of intake'),
        ),
    ]
