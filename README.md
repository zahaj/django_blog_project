# Full-Stack Django Portfolio Project

A comprehensive, full-stack web application built from scratch to serve as a personal developer portfolio. This project is built with a production-first mindset, featuring automated testing, cloud-based media storage (AWS S3), and a complete CI/CD pipeline for live deployment on Render.

[**Live Application Demo**](https://my-portfolio-rsms.onrender.com/)

## Features

* **Dynamic Project Showcase**: Full CRUD (Create, Read, Update, Delete) functionality for portfolio projects.
* **Secure Admin Operations**: All create, update, and delete operations are secured behind a user login (LoginRequiredMixin).
* **Cloud Media Storage**: All user-uploaded project images are handled by django-storages and stored securely in an AWS S3 bucket.
* **Automated Testing**: A comprehensive test suite built with pytest and pytest-django, testing views, models, and form logic.
* **Live Deployment**: The application is fully deployed and running live on Render (PaaS), served by a Gunicorn WSGI server.
* **Production-Grade Static Files**: Static assets (CSS/JS) are efficiently served in production using WhiteNoise.
* **Secure Email Notifications**: A working contact form that validates input and sends an email to the site admin using Django's email backend.
* **Responsive Design**: The frontend is built with Bootstrap 5 to be fully responsive and look great on all devices.

## Tech Stack

This project was built with a modern, professional stack:

* **Backend**: Python, Django
* **Frontend**: HTML5, CSS3, Bootstrap 5
* **Database**: PostgreSQL
* **Deployment (PaaS)**: Render
* **Application Server (WSGI)**: Gunicorn
* **Cloud Storage**: AWS S3 (for all media files)
* **Static Files**: WhiteNoise
* **Testing**: pytest, pytest-django
* **Security & Config**: python-dotenv for environment variables, CSRF Protection
* **Core Tools**: Git, GitHub

## Local Development Setup

To run this project on your local machine, follow these steps:

1. **Clone the Repository**:

    ```
    git clone https://github.com/zahaj/django-blog-project.git
    cd django-blog-project
    ```

2. **Create and Activate a Virtual Environment**:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Production and Development Dependencies**:

    ``` 
    pip install -r requirements-dev.txt
    ```

4. **Set Up Local Postgres Database**:

* Install PostgreSQL on your local machine.

* Create a new database (e.g., `portfolio_db`).

* Create a user with privileges for that database.

5. **Configure Environment Variables**:

* Create a .env file in the project root:

    ```
    touch .env
    ```

* Add your local configuration to the `.env` file:

    ```
    # Set to True for local development
    DEBUG=True

    # Generate a new Django key
    SECRET_KEY='your-local-secret-key'

    # Your local database URL
    DATABASE_URL='postgres://YOUR_DB_USER:YOUR_DB_PASSWORD@localhost:5432/portfolio_db'

    # Email for contact form
    ADMIN_EMAIL='your-email@gmail.com'
    DEFAULT_FROM_EMAIL='noreply@your-domain.com'

    # (Optional) You can use the live S3 keys for local media, or leave blank to use local storage
    AWS_ACCESS_KEY_ID=...
    AWS_SECRET_ACCESS_KEY=...
    AWS_STORAGE_BUCKET_NAME=...
    AWS_S3_REGION_NAME=...
    ```

6. **Run Database Migrations**:

    ```
    python manage.py migrate
    ```

7. **Seed the Database (Optional)**:

* You can run the custom seed command to populate the database with my primary projects:
    ```
    python manage.py seed_db
    ```

* Alternatively, create your own superuser to add content via the admin:
    ```
    python manage.py createsuperuser
    ```

8. **Run the Development Server**:

    ```
    python manage.py runserver
    ```

The project will be available at `http://127.0.0.1:8000/`.

9. **Run Tests:**

* Run the full test suite using `pytest`:

  ```
  pytest
  
  ```