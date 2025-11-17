"""
Forms for the 'projects' app.

This file defines the forms used for user input, including
the public-facing contact form and the admin-facing project creation form.
"""
from django import forms
from .models import Project

class ContactForm(forms.Form):
    """
    A simple form for site visitors to send a contact message.
    This form is not tied to a model and is processed in the 'contact' view.
    """
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        """
        Adds Bootstrap's 'form-control' class to all fields
        on initialization, so we don't need to do it in the template.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProjectForm(forms.ModelForm):
    """
    A ModelForm based on the Project model, used in the
    CreateView and UpdateView to manage projects from the frontend.
    """
    class Meta:
        model = Project
        fields = ('title', 'description', 'technologies', 'category', 'image', 'link')

    def __init__(self, *args, **kwargs):
        """
        Adds Bootstrap's 'form-control' class to all fields
        on initialization, except for the 'technologies' ManyToMany field
        which uses checkboxes.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'technologies':
                field.widget.attrs['class'] = 'form-control'