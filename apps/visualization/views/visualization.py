from django.shortcuts import render
from ..models import Survey
from django.db import connection
import pandas as pd


def index(request):
    return render(request, '../templates/visualization/index.html', {})


def survey_result(request):
    survey_getter = Survey()
    query = str(Survey.objects.all().query)
    survey = pd.read_sql_query(query, connection)
    data_dict = {'survey': survey}
    return render(request, '../templates/visualization/survey.html', data_dict)


