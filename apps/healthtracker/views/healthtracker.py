from django.urls import path
from django.shortcuts import render


def index(request):
    return render(request, '../templates/healthtracker/index.html', {})