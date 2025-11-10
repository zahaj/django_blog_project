from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('about/', views.about, name='about_me'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('technology/<str:name>/', views.technology_detail, name='technology_detail'),
    path('contact', views.contact, name='contact'),
    path('projects/add', views.ProjectCreateView.as_view(), name='project_add'),
    path('projects/<int:pk>/edit', views.ProjectUpdateView.as_view(), name="project_edit"),
    path('projects/<int:pk>/delete', views.ProjectDeleteView.as_view(), name="project_delete"),
]