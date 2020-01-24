# Generated by Django 3.0.1 on 2020-01-01 22:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dlcm2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionMed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_date', models.DateField(verbose_name='submission date')),
                ('med_time', models.TimeField(default=datetime.datetime(2020, 1, 1, 22, 26, 56, 965508, tzinfo=utc), verbose_name='Time of intake')),
                ('med_name', models.CharField(choices=[('OP', 'Olanzapine'), ('LP', 'Lorazepam')], max_length=2)),
                ('med_dose', models.DecimalField(decimal_places=2, max_digits=10)),
                ('med_dose_unit', models.CharField(choices=[('1', 'Milligram'), ('2', 'Gram'), ('3', 'Milliliter')], max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='SectionMedAnswers',
        ),
    ]
