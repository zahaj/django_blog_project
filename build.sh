#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput

echo "Creating superuser..."
python manage.py shell -c "import os; from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username=os.environ['DJANGO_SUPERUSER_USERNAME']).exists() or User.objects.create_superuser(username=os.environ['DJANGO_SUPERUSER_USERNAME'], email=os.environ['DJANGO_SUPERUSER_EMAIL'], password=os.environ['DJANGO_SUPERUSER_PASSWORD'])"