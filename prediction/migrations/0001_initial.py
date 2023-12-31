# Generated by Django 4.0.4 on 2022-06-07 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ALF', 'Alternaria Leaf Spot'), ('CAC', 'Cabbage Aphid Colony'), ('CR', 'Club Root'), ('RS', 'Ring Spot')], default='ALF', max_length=3, unique=True)),
                ('description', models.TextField()),
                ('serverity', models.IntegerField(choices=[(0, 'Low'), (1, 'Minor'), (2, 'Moderate'), (3, 'High'), (4, 'Critical')], default=0)),
                ('cure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prediction.cure')),
            ],
        ),
        migrations.CreateModel(
            name='RawImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prediction_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prediction.disease')),
                ('raw_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prediction.rawimage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
