from django.shortcuts import render
from ..models import MentalInfo, PhysicalInfo


def index(request):
    return render(request, '../templates/healthbook/index.html', {})


def physical_health(request):
    physicaldiseases = PhysicalInfo.objects.all()
    data_dict = {'physicaldiseases': physicaldiseases}
    return render(request, '../templates/healthbook/physicalhealth.html', data_dict)


def mental_health(request):
    mentaldiseases = MentalInfo.objects.all()
    data_dict = {'mentaldiseases': mentaldiseases}
    return render(request, '../templates/healthbook/mentalhealth.html', data_dict)


def physical_detail(request, physicalinfo_id):
    physicaldiseases = PhysicalInfo.objects.get(pk=physicalinfo_id)
    data_dict = {'physicaldiseases': physicaldiseases}
    return render(request, '../templates/healthbook/physicaldetail.html', data_dict)


def mental_detail(request, mentalinfo_id):
    mentaldiseases = MentalInfo.objects.get(pk=mentalinfo_id)
    data_dict = {'mentaldiseases': mentaldiseases}
    return render(request, '../templates/healthbook/mentaldetail.html', data_dict)
