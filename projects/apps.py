"""
App configuration for the 'projects' app.

This file defines the configuration class for the 'projects' app.
This class, 'ProjectsConfig', is referenced in the main
'settings.py' file under the INSTALLED_APPS list.
"""
from django.apps import AppConfig

class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'
