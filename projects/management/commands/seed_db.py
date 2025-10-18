from django.core.management.base import BaseCommand
from projects.models import Project, Category, Technology

class Command(BaseCommand):
    help = "Popluates a new database with some sample data by creating" \
    "a Category, Technology, and Project objects"

    def handle(self, *args, **options):
        Project.objects.create(
            title="Daily Briefing API",
            description="A containerized, tested, and authenticated backend service" \
            "built with Python and FastAPI. This project serves as a comprehensive " \
            "demonstration of professional backend development practices, from initial " \
            "design to automated CI/CD deployment."
        )
        Project.objects.create(
            title="Automatic filter identification for CCD images",
            description="The filter identification script for photometric CCD images from SAO." \
            "It automatically identifies the filter through which the CCD image was taken and" \
            "saves this information in fits header."
        )
        Technology.objects.create(name="Python")
        Technology.objects.create(name="Django")
        Technology.objects.create(name="FastAPI")
        Technology.objects.create(name="Docker")
        Technology.objects.create(name="C#")
        Category.objects.create(name="Web Development")
        Category.objects.create(name="Data Science")
        Category.objects.create(name="Mobile Apps")