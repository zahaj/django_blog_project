from django.shortcuts import render
from .models import Project

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