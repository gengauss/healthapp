# Generated by Django 3.1.1 on 2020-11-30 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0003_diabetes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='age',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='anxiety_disorder',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='bipolar_disorder',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='chronic_issue',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='chronic_issue_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='country',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='depression',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='diet',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='do_exercise',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='exercise_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='exercise_period',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='family_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='first_meal_time',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='friends_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='gender',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='job_school_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='last_meal_time',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='medical_checkup',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='mental_diseases',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='mental_effect',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='mental_important',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='money_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='no_of_meals',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='occupation',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='partner_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='same_time_meal',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='sleep_period',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='sleep_time',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='sns_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='stress',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='stress_relief',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='wake_up_time',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='water_per_day',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
