# Generated by Django 3.2.4 on 2021-08-30 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Automaton', '0002_auto_20210830_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='Email',
        ),
        migrations.AlterField(
            model_name='bookings',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 30, 15, 52, 38, 737229)),
        ),
    ]
