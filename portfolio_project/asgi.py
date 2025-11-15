"""
ASGI config for the portfolio_project project.

It exposes the ASGI callable as a module-level variable named ``application``.
This file is the entry point for ASGI-compatible web servers and enables
asynchronous features (which are not used in this project but are
supported by default).

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_asgi_application()
