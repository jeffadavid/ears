# Generated by Django 2.0 on 2019-08-19 08:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0034_idsr_weekly_report_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='idsr_weekly_national_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(default='000000', max_length=100)),
                ('data_value', models.CharField(max_length=50)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('idsr_disease_id', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='veoc.dhis_disease_data_elements')),
                ('org_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veoc.organizational_units')),
            ],
        ),
        migrations.RenameModel(
            old_name='idsr_weekly_report',
            new_name='idsr_weekly_facility_report',
        ),
    ]
