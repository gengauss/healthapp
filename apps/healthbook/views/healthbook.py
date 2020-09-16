from django.urls import path
from django.shortcuts import render


def index(request):
    return render(request, '../templates/healthbook/index.html', {})


def physical_health(request):
    return render(request, '../templates/healthbook/physicalhealth.html', {})


def mental_health(request):
    return render(request, '../templates/healthbook/mentalhealth.html', {})
