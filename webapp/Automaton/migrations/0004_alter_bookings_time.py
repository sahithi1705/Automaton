# Generated by Django 3.2.4 on 2021-08-31 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Automaton', '0003_auto_20210830_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 31, 16, 11, 51, 352051)),
        ),
    ]