"""
WSGI config for the portfolio_project project.

It exposes the WSGI callable as a module-level variable named application.
This file is the entry point for WSGI-compatible web servers (like Gunicorn)
to serve the application. WSGI (Web Server Gateway Interface) is the
standard for synchronous Python web applications.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()
