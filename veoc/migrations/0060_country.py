# Generated by Django 2.0 on 2020-03-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0059_auto_20200314_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_code', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('iso', models.CharField(max_length=50)),
                ('iso3', models.CharField(max_length=50)),
            ],
        ),
    ]
