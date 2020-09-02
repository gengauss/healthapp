from django.urls import path
from .views import healthbook

urlpatterns = [
    path('', healthbook.index, name="healthbook"),
]