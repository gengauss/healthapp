from django.shortcuts import redirect, render

from ..models import Goal
from ..forms import GoalForm


def listGoal(request):
    queryset = Goal.objects.order_by('complete', 'due')
    form = GoalForm()
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks': queryset,
        'form': form,
    }
    return render(request, '../templates/healthtracker/list_goal.html', context)
