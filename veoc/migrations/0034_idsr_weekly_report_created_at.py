# Generated by Django 2.0 on 2019-08-14 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0033_auto_20190814_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='idsr_weekly_report',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
