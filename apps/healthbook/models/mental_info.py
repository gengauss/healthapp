from django.contrib import admin
from django.db import models


class MentalInfo(models.Model):
    class Meta:
        db_table = 'mental_info'
        get_latest_by = 'created'