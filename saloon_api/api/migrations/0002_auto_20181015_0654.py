# Generated by Django 2.1.1 on 2018-10-15 06:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_time',
            field=models.DateField(default=datetime.datetime(2018, 10, 15, 6, 54, tzinfo=utc)),
        ),
    ]
