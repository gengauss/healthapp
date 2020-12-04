from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Profile, Goal


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(person_of=instance)
        print("profile created")


def create_goal(sender, instance, created, **kwargs):
    if created:
        Goal.objects.create(person_of=instance)
        print("profile created")


post_save.connect(create_profile, sender=User)
post_save.connect(create_goal, sender=User)
