from django.shortcuts import render

from .survey import plot_country, plot_age, plot_occupation, plot_gender, plot_water, plot_diet, plot_meals, \
    plot_meals, plot_first_meal, plot_last_meal, plot_same_meal
from .tools import plot_bar_chart
from ..models import Survey
from django.db import connection
import pandas as pd


def index(request):
    return render(request, '../templates/visualization/index.html', {})


def survey_result(request):
    query = str(Survey.objects.all().query)
    survey = pd.read_sql_query(query, connection)
    script_country, div_country = plot_country()
    script_age, div_age = plot_age()
    script_job, div_job = plot_occupation()
    script_gender, div_gender = plot_gender()
    script_water, div_water = plot_water()
    script_diet, div_diet = plot_diet()
    script_meals, div_meals = plot_meals()
    script_first_meal, div_first_meal = plot_first_meal()
    script_last_meal, div_last_meal = plot_last_meal()
    script_same_meal, div_same_meal = plot_same_meal()

    important_cols = survey['mental_important'].value_counts().keys().tolist()
    important_counts = survey['mental_important'].value_counts().tolist()
    mental_important = {'important': important_cols, 'counts': important_counts}
    mental_important_df = pd.DataFrame(mental_important)
    script_mental_important, div_mental_important = plot_bar_chart(mental_important_df['important'],
                                                                   mental_important_df['counts'])

    data_dict = {'survey': survey, 'script_country': script_country, 'div_country': div_country,
                 'script_age': script_age, 'div_age': div_age,
                 'script_job': script_job, 'div_job': div_job,
                 'script_gender': script_gender, 'div_gender': div_gender,
                 'script_water': script_water, 'div_water': div_water,
                 'script_diet': script_diet, 'div_diet': div_diet,
                 'script_meals': script_meals, 'div_meals': div_meals,
                 'script_first_meal': script_first_meal, 'div_first_meal': div_first_meal,
                 'script_last_meal': script_last_meal, 'div_last_meal': div_last_meal,
                 'script_same_meal': script_same_meal, 'div_same_meal': div_same_meal,
                 'script_mental_important': script_mental_important, 'div_mental_important': div_mental_important}
    return render(request, '../templates/visualization/survey.html', data_dict)
