# Generated by Django 3.2.4 on 2021-07-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='First_name',
            field=models.CharField(default='null', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='Last_name',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
