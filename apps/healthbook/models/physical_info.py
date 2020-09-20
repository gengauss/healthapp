from django.contrib import admin
from django.db import models


class PhysicalInfo(models.Model):
    class Meta:
        db_table = 'physical_info'
        get_latest_by = 'created'

    name = models.CharField(max_length=256, default=None)
    general_information = models.TextField(default=None)
    symptoms = models.TextField(default=None)
    prevention = models.TextField(default=None)
    treatment = models.TextField(default=None)


class PhysicalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'general_information', 'symptoms', 'prevention', 'treatment')


admin.site.register(PhysicalInfo, PhysicalInfoAdmin)
