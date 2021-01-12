from django.shortcuts import render
from .models import Chapter, Subsection, Requirement
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def project(request):
    return render(request, 'project.html', {'title': 'Project'})


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
