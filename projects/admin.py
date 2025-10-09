from django.contrib import admin

from .models import Project, Technology

class ProjectAdmin(admin.ModelAdmin):
    # This adds a nice, filterable selection box for technologies
    filter_horizontal = ('technologies',)

# Register your models here.
# Unregister the old simple registration if it exists, and re-register with the admin class
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)