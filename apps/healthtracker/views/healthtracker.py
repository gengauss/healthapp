from django.contrib import messages
from django.shortcuts import render, redirect

from ..forms import UserRegisterForm


def index(request):
    return render(request, '../templates/healthtracker/index.html', {})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('healthtracker')
    else:
        form = UserRegisterForm()
    return render(request, '../templates/healthtracker/register.html', {'form': form})
