# Generated by Django 3.1.1 on 2020-12-03 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0007_depression'),
    ]

    operations = [
        migrations.AddField(
            model_name='depression',
            name='number_support',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='depression',
            name='relationship_with_family',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='depression',
            name='relationship_with_friend',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='depression',
            name='relationship_with_husband',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]