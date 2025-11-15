#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This script serves as the primary entry point for managing the Django project.
It automatically sets the 'DJANGO_SETTINGS_MODULE' environment variable
to point to the project's settings file.

Common commands:
- python manage.py runserver: Starts the development server.
- python manage.py migrate: Applies database migrations.
- python manage.py makemigrations: Creates new migration files based on model changes.
- python manage.py shell: Opens an interactive Python shell with the project loaded.
- python manage.py createsuperuser: Creates a new admin user.
- python manage.py collectstatic: Collects static files into STATIC_ROOT.
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
