# Generated by Django 2.0 on 2020-08-01 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0105_auto_20200731_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline_quarantine',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 189030)),
        ),
        migrations.AlterField(
            model_name='airline_quarantine',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 189030)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='api_access_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 176064)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 176064)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='date_tested',
            field=models.DateField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 176064)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 176064)),
        ),
        migrations.AlterField(
            model_name='discharged_quarantine',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 179056)),
        ),
        migrations.AlterField(
            model_name='home_based_care',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 178059)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 172075)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 172075)),
        ),
        migrations.AlterField(
            model_name='quarantine_follow_up',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 173072)),
        ),
        migrations.AlterField(
            model_name='quarantine_revisit',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 176064)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 178059)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_lab_confirmation',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 178059)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_specimen_collected',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 178059)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='onset_of_symptoms',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 178059)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 8, 27, 1, 178059)),
        ),
    ]
