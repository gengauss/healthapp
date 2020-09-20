from django.contrib import admin
from django.db import models


class Survey(models.Model):
    class Meta:
        db_table = 'surveys'
        get_latest_by = 'created'

    timestamp = models.DateTimeField()
    # General
    country = models.CharField(max_length=256)
    age = models.CharField(max_length=256)
    occupation = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    # Physical Health
    water_per_day = models.CharField(max_length=256)
    diet = models.CharField(max_length=256)
    no_of_meals = models.CharField(max_length=256)
    first_meal_time = models.CharField(max_length=256)
    last_meal_time = models.CharField(max_length=256)
    same_time_meal = models.CharField(max_length=256)
    do_exercise = models.CharField(max_length=256)
    exercise_period = models.CharField(max_length=256)
    exercise_detail = models.TextField()
    sleep_period = models.CharField(max_length=256)
    sleep_time = models.CharField(max_length=256)
    wake_up_time = models.CharField(max_length=256)
    medical_checkup = models.CharField(max_length=256)
    chronic_issue = models.CharField(max_length=256)
    chronic_issue_detail = models.TextField()
    # Mental Health
    mental_important = models.IntegerField()
    mental_effect = models.IntegerField()
    stress = models.CharField(max_length=256)
    stress_relief = models.TextField()
    job_school_rate = models.IntegerField()
    family_rate = models.IntegerField()
    friends_rate = models.IntegerField()
    partner_rate = models.IntegerField()
    sns_rate = models.IntegerField()
    money_rate = models.IntegerField()
    depression = models.CharField(max_length=256)
    anxiety_disorder = models.CharField(max_length=256)
    bipolar_disorder = models.CharField(max_length=256)
    mental_diseases = models.CharField(max_length=256)
    mental_detail = models.TextField()


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'country', 'age', 'occupation', 'gender')


admin.site.register(Survey, SurveyAdmin)
