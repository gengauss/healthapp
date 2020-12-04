from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import MentalInfo, PhysicalInfo, Contact


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


def physical_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        physicaldiseases = PhysicalInfo.objects.filter(name__icontains=q)
        return render(request, '../templates/healthbook/physicalsearch.html',
                      {'physicaldiseases': physicaldiseases, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def mental_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        mentaldiseases = MentalInfo.objects.filter(name__icontains=q)
        return render(request, '../templates/healthbook/mentalsearch.html',
                      {'mentaldiseases': mentaldiseases, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def contact(request):
    if request.method == 'POST':
        contact_form = Contact(name=request.POST['name'], email=request.POST['email'], feedback=request.POST['feedback'])
        contact_form.save()
    return render(request, '../templates/home/contact.html', {})
