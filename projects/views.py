import imp
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
projectsList = [
    {
        'id':"1",
        'title':'Ecomerece',
        'description': 'Ecomerece Website',
    },
    {
        'id':'2',
        'title':'Ecomerece',
        'description': 'Ecomerece Website',
    },
    {
        'id':'3',
        'title':'Ecomerece',
        'description': 'Ecomerece Website',
    },
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj
    print(projectObj , "xxxxxxxxxxxxxxxxxx")
    return render(request, 'projects/single-project.html', {'project' : projectObj})