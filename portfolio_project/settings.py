"""
Django settings for portfolio_project project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core Settings ---
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
LOGIN_URL = '/admin/login/'

ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'your-default@email.com')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@yourdomain.com')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# --- Application Definitions ---
INSTALLED_APPS = [
    'projects.apps.ProjectsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_project.wsgi.application'


# --- Database ---
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=False,
        conn_health_checks=True,
    )
}


# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Storage, Static, and Media File Logic ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# --- Environment-Specific Settings (Storage, Media, Email) ---

if DEBUG:
    # --- DEVELOPMENT SETTINGS ---

    # Local file storage for media
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        }
    }

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

else:
    # --- PRODUCTION SETTINGS ---

    ALLOWED_HOSTS.extend([
        '.onrender.com',
        'my-portfolio-rsms.onrender.com'
    ])

    STATIC_ROOT = BASE_DIR / 'staticfiles'

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_FILE_OVERWRITE = False
    AWS_S3_SIGNATURE_VERSION = "s3v4"

    if AWS_STORAGE_BUCKET_NAME and AWS_S3_REGION_NAME:
        AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)
    else:
        AWS_S3_CUSTOM_DOMAIN = None

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_PORT = 465
    EMAIL_USE_TLS = False
    EMAIL_USE_SSL = True
    EMAIL_HOST_USER = "apikey"
    EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")
    DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
    ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")

    EMAIL_TIMEOUT = 10

# --- Default Auto Field ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'