# Generated by Django 4.0.4 on 2022-09-21 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_rename_serverity_disease_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]