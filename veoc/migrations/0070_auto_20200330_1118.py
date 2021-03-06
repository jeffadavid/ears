# Generated by Django 2.0 on 2020-03-30 08:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0069_auto_20200324_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarantine_contacts',
            name='cormobidity',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='quarantine_contacts',
            name='drugs',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='quarantine_contacts',
            name='nationality',
            field=models.ForeignKey(default='2620', on_delete=django.db.models.deletion.CASCADE, related_name='quarantine_nationality', to='veoc.organizational_units'),
        ),
        migrations.AddField(
            model_name='quarantine_contacts',
            name='nok',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='quarantine_contacts',
            name='nok_phone_num',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{10,15}$')]),
        ),
    ]
