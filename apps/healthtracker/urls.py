from django.urls import path
from .views import healthtracker

urlpatterns = [
    path('', healthtracker.index, name="healthtracker"),
]