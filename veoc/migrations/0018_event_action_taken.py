# Generated by Django 2.0 on 2019-06-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0017_auto_20190618_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='action_taken',
            field=models.TextField(default='None', max_length=500),
        ),
    ]
