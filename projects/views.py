from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Project, Technology
from .forms import ContactForm, ProjectForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

def contact(request):
    if request.method == 'POST':
        # This is a POST request, so process the form data
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # --- Build and send the email ---
            subject = f"New Contact Form Submission from {name}"
            email_message = f"""
            You received a new message from your portfolio site:

            From: {name}
            Email: {email}

            Message:
            {message}
            """
            send_mail(
                subject,
                email_message,
                'contact-form@domain.com', # "From" email
                ['e.zahajkiewicz@gmail.com'],      # "To" email (list)
            )

            # For now, we'll keep the print statement for a quick check
            print(f'New Message from {name} ({email}): {message}')

            # Redirect to a new URL to prevent form re-submission
            return redirect('project_index')
        else:
            print("Form invalid!")
            print(form.errors.as_data())
    else:
        # This is a GET request, so create a blank form
        form = ContactForm()
        
    context = {
        'form': form
    }
    return render(request, 'projects/contact.html', context)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_index') # Where to go after success
    
    # This ensures the 'login_required' mixin knows where to redirect
    login_url = '/admin/login'

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_index')

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    # form_class = ProjectForm
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_index')
    login_url = '/admin/login/'
