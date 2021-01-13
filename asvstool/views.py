from django.shortcuts import render
from .models import Chapter, Subsection, Requirement, Project, ReqsProject
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def project(request):
    context = {
        'Obiekty': Project.objects.all().filter(owner=request.user),
        'title': 'Project'
    }
    return render(request, 'project.html', context)

@login_required
def details_project(request, id):
    context = {
        'Name': Project.objects.get(id=id).project_name,
        'project': Project.objects.get(id=id),
        'title': 'Project Details'
    }
    return render(request, 'details.html', context)


@login_required
def details_project_req(request, id, id_state):
    if id_state < 15:
        chapter = Chapter.objects.get(id=id_state).chapter_title
    else:
        chapter = 'Rejected requirements'
    if request.method == "POST":
        req = ReqsProject.objects.get(id=request.POST.get('id'))
    context = {
        'Name': Project.objects.get(id=id).project_name,
        'project': Project.objects.get(id=id),
        'chapter': chapter,
        'Obiekty': ReqsProject.objects.all().filter(project=id),
        'title': 'Project Details'
    }
    return render(request, 'details_req.html', context)


@login_required
def about(request):
    context = {
        'Obiekty': Chapter.objects.all(),
        'title': 'About'
    }
    return render(request, 'about.html', context)


@login_required
def subsection(request, pk):
    context = {
        'Obiekty': Subsection.objects.all().filter(chapter_nr_id=pk),
        'Name': Chapter.objects.get(id=pk).chapter_title,
        'title': 'Subsection'
    }
    return render(request, 'subsection.html', context)


@login_required
def tests(request, pk):
    context = {
        'Obiekty': Requirement.objects.all().filter(subsection_nr_id=pk).order_by('pk'),
        'Name': Subsection.objects.get(id=pk).subsection_name,
        'title': 'Tests'
    }
    return render(request, 'tests.html', context)
