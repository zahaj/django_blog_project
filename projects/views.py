from django.shortcuts import render, get_object_or_404
from .models import Project, Technology

# Create your views here.
def project_index(request):
    # This query retrieves all Project objects from the database
    projects = Project.objects.all()
    
    # The context dictionary is used to pass data to the template
    context = {
        # If a variable doesn't exist in the template, Django just treats it
        # as empty and fails silently. The names in the context dictionary must match
        # the variables used in the template.
        'projects': projects
    }

    # render() combines the template with the context data and returns an HttpResponse
    return render(request, 'projects/project_index.html', context)

def about(request):
    return render(request, 'projects/about.html')

def project_detail(request, pk):
    # project = Project.objects.get()
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)

def technology_detail(request, name):
    technology = get_object_or_404(Technology, name__iexact=name)
    projects = technology.project_set.all()
    context = {
        'technology': technology,
        'projects': projects
    }
    return render(request, 'projects/technology_detail.html', context)