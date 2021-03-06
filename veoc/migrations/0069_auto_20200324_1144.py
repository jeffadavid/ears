# Generated by Django 2.0 on 2020-03-24 08:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0068_auto_20200324_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{10,15}$')]),
        ),
    ]
