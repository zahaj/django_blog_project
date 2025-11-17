"""
URL configuration for portfolio_project project.
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from projects import views as project_views

router = routers.DefaultRouter()
router.register(r'projects', project_views.ProjectViewSet, basename='project')
router.register(r'technologies', project_views.TechnologyViewSet, basename='technology')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Include all URLs from the 'projects' app
    path('', include('projects.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
