# dvdrental_project/settings.py  
from pathlib import Path  
import os  
  
# Build paths inside the project like this: BASE_DIR / 'subdir'  
BASE_DIR = Path(__file__).resolve().parent.parent  
  
# Quick-start development settings - unsuitable for production  
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/  
  
# SECURITY WARNING: keep the secret key used in production secret!  
SECRET_KEY = 'And1m0n4'  # Make sure to use your actual secret key  
  
# SECURITY WARNING: don't run with debug turned on in production!  
DEBUG = True  
  
ALLOWED_HOSTS = []  
  
# Application definition  
INSTALLED_APPS = [  
    'django.contrib.admin',  
    'django.contrib.auth',  
    'django.contrib.contenttypes',  
    'django.contrib.sessions',  
    'django.contrib.messages',  
    'django.contrib.staticfiles',  
    'dvdrental_prediction',  
]  
  
MIDDLEWARE = [  
    'django.middleware.security.SecurityMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',  
    'django.middleware.common.CommonMiddleware',  
    'django.middleware.csrf.CsrfViewMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware',  
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  
]  
  
ROOT_URLCONF = 'dvdrental_project.urls'  
  
TEMPLATES = [  
    {  
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  
        'DIRS': [BASE_DIR/'templates'],  
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
  
WSGI_APPLICATION = 'dvdrental_project.wsgi.application'  
  
# Database  
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases  
  
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.sqlite3',  
        'NAME': BASE_DIR / 'db.sqlite3',  
    }  
}  
  
# Static files (CSS, JavaScript, Images)  
STATIC_URL = 'static/'  
STATICFILES_DIRS = [  
    BASE_DIR / "static",  
]  
STATIC_ROOT = BASE_DIR / 'staticfiles'  
  
# Default primary key field type  
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  