from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

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
    msg = "Hello, you are on the projects page"
    number = 12
    context = {'message': msg , 'number' : number , 'projects' : projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectsObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectsObj = i
    return render(request, 'projects/single-project.html', {'project' : projectsObj})