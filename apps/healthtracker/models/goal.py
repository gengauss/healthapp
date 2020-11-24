from django.contrib import admin
from django.db import models


class Goal(models.Model):
    class Meta:
        db_table = 'goal'
        get_latest_by = 'created'

    title = models.CharField(max_length=256)
    complete = models.BooleanField(default=None)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.title


admin.site.register(Goal)
