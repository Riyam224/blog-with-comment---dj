from django.shortcuts import render

# Create your views here.
from .models import Project


def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'home.html', context)


def details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'details.html', context)
