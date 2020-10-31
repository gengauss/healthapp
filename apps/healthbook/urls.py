from django.urls import path
from .views import healthbook

urlpatterns = [
    path('', healthbook.index, name="healthbook"),
    path('physicalhealthinfo', healthbook.physical_health, name='physicalhealthinfo'),
    path('mentalhealthinfo', healthbook.mental_health, name='mentalhealthinfo'),
    path('mentalhealthinfo/<int:mentalinfo_id>', healthbook.mental_detail, name='mentaldetail'),
    path('physicalhealthinfo/<int:physicalinfo_id>', healthbook.physical_detail, name='physicaldetail')
]
