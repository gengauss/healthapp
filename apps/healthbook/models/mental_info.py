from django.contrib import admin
from django.db import models


class MentalInfo(models.Model):
    class Meta:
        db_table = 'mental_info'
        get_latest_by = 'created'

    general_information = models.TextField(default=None)
    symptoms = models.TextField(default=None)
    prevention = models.TextField(default=None)
    treatment = models.TextField(default=None)


class MentalInfoAdmin(admin.ModelAdmin):
    list_display = ('general_information', 'symptoms', 'prevention', 'treatment')


admin.site.register(MentalInfo, MentalInfoAdmin)
