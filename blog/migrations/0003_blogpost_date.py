# Generated by Django 3.2.1 on 2021-06-01 09:40

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210531_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=datetime.datetime.today),
            preserve_default=False,
        ),
    ]
