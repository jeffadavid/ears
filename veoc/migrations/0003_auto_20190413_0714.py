# Generated by Django 2.0 on 2019-04-13 04:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veoc', '0002_auto_20190314_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='incident_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_description', models.CharField(max_length=100)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('updated_at', models.DateField(default=datetime.date.today)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incident_type_updated_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incident_type_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='call_log',
            name='incident_type',
        ),
        migrations.AlterField(
            model_name='call_log',
            name='incident_status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='veoc.incident_status'),
        ),
        migrations.AlterField(
            model_name='call_log',
            name='reporting_region',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='veoc.reporting_region'),
        ),
    ]
