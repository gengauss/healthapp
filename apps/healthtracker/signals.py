from django.db.models.signals import post_save
from django.contrib.auth.models import User
from apps.healthtracker.models import Profile


def create_profile(instance, created):
    if created:
        Profile.objects.create(person_of=instance)
        print("profile created")


post_save.connect(create_profile, sender=User)
