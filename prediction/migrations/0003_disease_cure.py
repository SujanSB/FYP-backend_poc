# Generated by Django 4.0.4 on 2022-06-07 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_remove_disease_cure'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='cure',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prediction.cure'),
            preserve_default=False,
        ),
    ]
