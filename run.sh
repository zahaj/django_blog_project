#!/bin/bash

# This script runs the production workflow

echo "Running database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
gunicorn portfolio_project.wsgi