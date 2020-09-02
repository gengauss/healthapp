from django.shortcuts import render


def index(request):
    return render(request, '../templates/visualization/index.html', {})
