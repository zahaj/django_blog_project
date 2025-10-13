from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('about/', views.about, name='about_me')
]