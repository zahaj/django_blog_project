from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('about/', views.about, name='about_me'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('technology/<str:name>/', views.technology_detail, name='technology_detail')

]