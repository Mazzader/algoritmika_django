import random
import string

from django.shortcuts import render, redirect
from django.views import View
from .forms import SolveForm
from .models import Task, Student, Solve
from django.core.exceptions import ValidationError

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TaskView(View):
    """Список заданий"""
    def get(self, request):
        tasks = Task.objects.all()[:6]
        students = Student.objects.all()
        return render(request, 'main/index.html', {"tasks_list": tasks, "students_list": students})


class SolveTask(View):
    """Решить задачу"""
    def get(self, request,pk):
        solve = Solve.objects.get(id=pk)
        form = SolveForm(request.GET)
        return render(request,"main/solve.html", {"solve": solve,"form": form})

    def post(self, request,pk):
        form = SolveForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            new_solve = Solve(student=form.cleaned_data['student'],
                              task=form.cleaned_data['task'],
                              score=0,
                              text=form.cleaned_data['text'],
                              slug=id_generator(8))
            new_solve.save()
            return redirect('/')
        else:
            raise ValidationError

