from django.contrib import admin

from .models import Project, Technology # Import the Project model

# Register your models here.
admin.site.register(Project)
admin.site.register(Technology)