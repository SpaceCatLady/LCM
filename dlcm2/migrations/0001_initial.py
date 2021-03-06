# Generated by Django 3.0.1 on 2020-01-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SectionMedAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_date', models.DateField(verbose_name='submission date')),
                ('med_time', models.TimeField(verbose_name='med_time_taken')),
                ('med_name', models.CharField(max_length=200)),
                ('med_dose', models.DecimalField(decimal_places=2, max_digits=10)),
                ('med_dose_unit', models.CharField(max_length=5)),
            ],
        ),
    ]
