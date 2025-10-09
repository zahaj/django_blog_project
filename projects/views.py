from django.shortcuts import render
from .models import Project

# Create your views here.
def project_index(request):
    # This query retrieves all Project objects from the database
    projects = Project.objects.all()
    
    # The context dictionary is used to pass data to the template
    context = {
        'projects': projects
    }

    # render() combines the template with the context data and returns an HttpResponse
    return render(request, 'projects/project_index.html', context)