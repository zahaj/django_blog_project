"""
URL patterns for the 'projects' app.

This file defines the application-specific URLs, which are then 
included by the main project's urls.py.
"""
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    
    # Core pages
    path('', views.project_index, name='project_index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Technology
    path('technologies/<str:name>/', views.technology_detail, name='technology_detail'),

    # Project CRUD
    path('projects/add/', views.ProjectCreateView.as_view(), name='project_add'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name="project_edit"),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name="project_delete"),
]