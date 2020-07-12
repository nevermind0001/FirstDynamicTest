from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

tasks = []

def index(request):
    return render(request, "introne/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("introne:index"))
        else:
            return render(request, "introne/add.html", {
                "form": form
            })
    return render(request, "introne/add.html",{
        "form": NewTaskForm()
    })

