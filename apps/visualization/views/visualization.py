import pandas as pd
from django.db import connection
from django.shortcuts import render

from .survey import plot_country, plot_age, plot_occupation, plot_gender, plot_water, plot_diet, plot_meals, \
    plot_first_meal, plot_last_meal, plot_same_meal
from .tools import plot_bar_chart, plot_count, plot_hexbin, plot_hist, plot_stacked_bar, plot_line
from ..models import Survey, Diabetes
import numpy as np
import pandas_bokeh


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
                                                                   mental_important_df['counts'],
                                                                   title="Mental Health Importance")

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


def diabetes_result(request):
    query = str(Diabetes.objects.all().query)
    diabetes = pd.read_sql_query(query, connection)

    # tested
    tested_cols = diabetes['tested'].value_counts().keys().tolist()
    tested_counts = diabetes['tested'].value_counts().tolist()
    tested = {'tested': tested_cols, 'counts': tested_counts}
    tested_df = pd.DataFrame(tested)
    script_tested, div_tested = plot_count(tested_df['tested'], tested_df['counts'], "Tested Counts")

    # age
    age = diabetes['age'].value_counts().tolist()
    script_age, div_age = plot_count(tested_cols, age, "Age")

    # insu
    x = np.array(diabetes['insu'])
    y = np.array(diabetes['age'])
    title = "Hexbin for insulin and age"
    script_insu, div_insu = plot_hexbin(x, y, title)

    # age distribution
    df_dist = pd.DataFrame({
        'tested_positive': diabetes["age"][diabetes['tested'] == 'tested_positive'],
        'tested_negative': diabetes["age"][diabetes['tested'] == 'tested_negative']
    }, columns=['tested_positive', 'tested_negative'])

    script_dist, div_dist = plot_hist(df_dist, "Age distribution")

    labels = ['Unhealthy', 'Healthy', 'Overweight', 'Obese']
    tested = ['tested_positive', 'tested_negative']
    data = {'labels': labels,
            'tested_positive': [2, 7, 44, 215],
            'tested_negative': [9, 105, 136, 250]}
    script_stacked, div_stacked = plot_stacked_bar(labels, tested, data, "")

    script_line, div_line = plot_line(diabetes[diabetes['tested'] == 'tested_positive']['age'],
                                      diabetes[diabetes['tested'] == 'tested_positive']['insu'])

    data_dict = {'script_tested': script_tested, 'div_tested': div_tested,
                 'script_age': script_age, 'div_age': div_age,
                 'script_insu': script_insu, 'div_insu': div_insu,
                 'script_dist': script_dist, 'div_dist': div_dist,
                 'script_stacked': script_stacked, 'div_stacked': div_stacked,
                 'script_line': script_line, 'div_line': div_line}
    return render(request, '../templates/visualization/diabetes.html', data_dict)
