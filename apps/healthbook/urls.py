from django.urls import path
from .views import healthbook

urlpatterns = [
    path('', healthbook.index, name="healthbook"),
    path('physicalhealth', healthbook.physical_health, name='physicalhealth'),
    path('mentalhealth', healthbook.mental_health, name='mentalhealth'),
]