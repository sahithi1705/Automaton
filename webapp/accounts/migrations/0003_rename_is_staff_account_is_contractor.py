# Generated by Django 3.2.4 on 2021-07-07 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210707_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_staff',
            new_name='is_contractor',
        ),
    ]
