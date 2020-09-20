from django.urls import path
from .views import visualization

urlpatterns = [
    path('', visualization.index, name="visualization"),
    path('surveyresult', visualization.survey_result, name='surveyresult'),
]