# Generated by Django 2.2.7 on 2020-09-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthbook', '0002_auto_20200908_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalinfo',
            name='name',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='physicalinfo',
            name='name',
            field=models.CharField(default=None, max_length=256),
        ),
    ]