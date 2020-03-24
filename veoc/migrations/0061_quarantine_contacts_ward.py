# Generated by Django 2.0 on 2020-03-14 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0060_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarantine_contacts',
            name='ward',
            field=models.ForeignKey(blank=True, default='2620', on_delete=django.db.models.deletion.CASCADE, related_name='quarantine_ward', to='veoc.organizational_units'),
        ),
    ]