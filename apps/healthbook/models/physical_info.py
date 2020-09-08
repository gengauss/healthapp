from django.contrib import admin
from django.db import models


class PhysicalInfo(models.Model):
    class Meta:
        db_table = 'physical_info'
        get_latest_by = 'created'