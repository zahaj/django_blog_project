FROM python:3.11-slim

# Prevents Python from buffering output, so logs show up in real-time.
ENV PYTHONUNBUFFERED=1
# Tells Gunicorn where to find the app.
ENV APP_PORT=8000

# All commands from now on will run from /app.
WORKDIR /app

COPY requirements.txt requirements-dev.txt /app/

# Install *only* the production dependencies.
RUN pip install -r requirements.txt

# Copy everything that isn't in .dockerignore into /app
COPY . .
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

EXPOSE 8000

CMD ["gunicorn", "portfolio_project.wsgi", "--bind", "0.0.0.0:8000"]