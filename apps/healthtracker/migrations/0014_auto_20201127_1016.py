# Generated by Django 3.1.1 on 2020-11-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthtracker', '0013_auto_20201127_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='due',
            field=models.DateTimeField(default='2020-01-01'),
        ),
    ]
