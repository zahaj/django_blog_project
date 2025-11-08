from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('about/', views.about, name='about_me'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('technology/<str:name>/', views.technology_detail, name='technology_detail'),
    path('contact', views.contact, name='contact'),
    path('project/add', views.ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/edit', views.ProjectUpdateView.as_view(), name="project_edit"),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name="project_delete"),
]