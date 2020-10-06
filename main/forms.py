from django import forms
from .models import Solve, Task, Student

class SolveForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    task = forms.ModelChoiceField(queryset=Task.objects.all())
    score = 0
    text = forms.CharField(widget=forms.Textarea)
    slug = 0

    class Meta:
        model = Solve

    widgets = {
        "class": "form-control"
    }