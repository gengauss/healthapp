# Generated by Django 3.1.1 on 2020-11-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthbook', '0004_auto_20201119_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalinfo',
            name='cause',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='mentalinfo',
            name='diagnosis',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='mentalinfo',
            name='url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mentalinfo',
            name='general_information',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mentalinfo',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mentalinfo',
            name='prevention',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mentalinfo',
            name='symptoms',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mentalinfo',
            name='treatment',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
