# Generated by Django 3.2.4 on 2021-07-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_contractor',
        ),
    ]
