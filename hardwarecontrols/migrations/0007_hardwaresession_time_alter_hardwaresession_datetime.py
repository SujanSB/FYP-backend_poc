# Generated by Django 4.0.4 on 2022-09-21 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hardwarecontrols', '0006_hardwaresession_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardwaresession',
            name='time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 21, 13, 18, 24, 92351, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hardwaresession',
            name='datetime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
