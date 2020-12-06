# Generated by Django 3.1.1 on 2020-12-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthbook', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hb_content', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('hb_design', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('hb_change', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('hb_feedback', models.TextField(blank=True, null=True)),
                ('vs_content', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('vs_design', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('vs_change', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('vs_feedback', models.TextField(blank=True, null=True)),
                ('fr_design', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('fr_use', models.CharField(choices=[('1日以下', '1日以下'), ('3日間', '3日間'), ('1週間以内', '1週間以内'), ('2週間以内', '2週間以内'), ('1ヵ月以上', '1ヵ月以上')], default='None', max_length=6)),
                ('fr_opinion', models.TextField(blank=True, null=True)),
                ('fr_change', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('fr_feedback', models.TextField(blank=True, null=True)),
                ('ct_design', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('ct_use', models.CharField(choices=[('1日以下', '1日以下'), ('3日間', '3日間'), ('1週間以内', '1週間以内'), ('2週間以内', '2週間以内'), ('1ヵ月以上', '1ヵ月以上')], default='None', max_length=6)),
                ('ct_opinion', models.TextField(blank=True, null=True)),
                ('ct_change', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('ct_feedback', models.TextField(blank=True, null=True)),
                ('hg_design', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('hg_use', models.CharField(choices=[('1日以下', '1日以下'), ('3日間', '3日間'), ('1週間以内', '1週間以内'), ('2週間以内', '2週間以内'), ('1ヵ月以上', '1ヵ月以上')], default='None', max_length=6)),
                ('hg_opinion', models.TextField(blank=True, null=True)),
                ('hg_change', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='None', max_length=6)),
                ('hg_feedback', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'feedback',
                'get_latest_by': 'created',
            },
        ),
    ]