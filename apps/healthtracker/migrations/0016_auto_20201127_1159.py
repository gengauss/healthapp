# Generated by Django 3.1.1 on 2020-11-27 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthtracker', '0015_auto_20201127_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='answer',
            new_name='text',
        ),
    ]
