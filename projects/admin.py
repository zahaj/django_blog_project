"""
Admin configuration for the 'projects' app.

This file registers models with the Django admin interface and
defines custom ModelAdmin classes to improve the admin experience.
"""
from django.contrib import admin
from .models import Project, Technology, Category

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Project model.
    """
    # Columns to display in the admin list view
    list_display = ('title', 'link', 'created_at', 'category',)

    # Fields to include in the admin search bar
    search_fields = ('title', 'description',)

    # Use a horizontal filter widget for the ManyToMany 'technologies' field
    filter_horizontal = ('technologies',)

# Register the other models with the default admin interface
admin.site.register(Technology)
admin.site.register(Category)