# Generated by Django 2.0 on 2020-03-14 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0057_quarantine_follow_up_follow_up_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quarantine_follow_up',
            name='test_day',
        ),
    ]
