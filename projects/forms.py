from django import forms
from .models import Project

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'technologies', 'category', 'image', 'link')
        # exclude = ('technologies',)