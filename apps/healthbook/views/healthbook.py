from django.shortcuts import render
from ..models import MentalInfo


def index(request):
    return render(request, '../templates/healthbook/index.html', {})


def physical_health(request):
    return render(request, '../templates/healthbook/physicalhealth.html', {})


def mental_health(request):
    mentaldiseases = MentalInfo.objects.all()
    data_dict = {'mentaldiseases': mentaldiseases}
    return render(request, '../templates/healthbook/mentalhealth.html', data_dict)


def mental_detail(request, mentalinfo_id):
    mentaldiseases = MentalInfo.objects.get(pk=mentalinfo_id)
    data_dict = {'mentaldiseases': mentaldiseases}
    return render(request, '../templates/healthbook/detail.html', data_dict)
