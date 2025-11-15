"""
Custom Django management command to seed the database
with initial data (Categories, Technologies, and Projects).
"""
from django.core.management.base import BaseCommand
from projects.models import Project, Category, Technology

class Command(BaseCommand):
    help = "Popluates a new database with initial, essential data."

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # --- Create Categories ---
        # get_or_create returns (object, created_boolean)
        web_dev_cat, _ = Category.objects.get_or_create(name="Web Development")
        data_sci_cat, _ = Category.objects.get_or_create(name="Data Science")

        # --- Create Technologies ---
        py, _ = Technology.objects.get_or_create(name="Python")
        dj, _ = Technology.objects.get_or_create(name="Django")
        fa, _ = Technology.objects.get_or_create(name="FastAPI")
        dock, _ = Technology.objects.get_or_create(name="Docker")
        s3, _ = Technology.objects.get_or_create(name="AWS S3")
        render, _ = Technology.objects.get_or_create(name="Render")
        pytest, _ = Technology.objects.get_or_create(name="Pytest")
        sql, _ = Technology.objects.get_or_create(name="PostgreSQL")
 
        # --- Create Project 1 (This Portfolio) ---
        proj1, created = Project.objects.get_or_create(
            title="Full-Stack Django Portfolio",
            defaults={
                'description': (
                    "The website you are currently on. A full-stack, production-grade "
                    "web application built from scratch. It features a complete CRUD "
                    "interface, a secure contact form, a full test suite with Pytest, "
                    "and a professional CI/CD pipeline. Deployed on Render, serving "
                    "static files via WhiteNoise and media via AWS S3."
                ),
                'link': "https://github.com/zahaj/django-blog-project",
                'category': web_dev_cat,
            }
        )
        if created:
            proj1.technologies.add(py, dj, sql, pytest, s3, render)
            self.stdout.write(self.style.SUCCESS('Successfully created Portfolio project.'))

        # --- Create Project 2 (FastAPI) ---
        proj2, created = Project.objects.get_or_create(
            title="Daily Briefing API",
            defaults={
                'description': (
                    "A containerized, tested, and authenticated backend service "
                    "built with Python and FastAPI. This project serves as a comprehensive "
                    "demonstration of professional backend development practices, from "
                    "initial design to automated CI/CD deployment."
                ),
                'link': "https://github.com/zahaj/fastapi-briefing-api", # Change to your repo
                'category': web_dev_cat,
            }
        )
        if created:
            proj2.technologies.add(py, fa, dock, pytest)
            self.stdout.write(self.style.SUCCESS('Successfully created FastAPI project.'))

        self.stdout.write(self.style.SUCCESS('Database seeding complete.'))