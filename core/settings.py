"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from dotenv import load_dotenv
import sys


load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTING = sys.argv[1:2] == ['test']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's#1rr4vq$@ug^j!0y91zokyytog^$f$1c@alnp3=@2qj0s9%4%'

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

    'rest_framework',
    'logpipe',
    'django_extensions',

    'ticketing',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        }
    }
}

LOGPIPE = {
    'OFFSET_BACKEND': 'logpipe.backend.kafka.ModelOffsetStore',
    'CONSUMER_BACKEND': 'logpipe.backend.kafka.Consumer',
    'PRODUCER_BACKEND': 'logpipe.backend.kafka.Producer',
    'KAFKA_BOOTSTRAP_SERVERS': [
        os.getenv('KAFKA_SERVER', 'localhost:9092')
    ],
    'KAFKA_CONSUMER_KWARGS': {
        'group_id': 'django-logpipe',
    },
    'DEFAULT_FORMAT': 'json'
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'ticketing'),
        'USER': os.environ.get('DATABASE_USER', 'ticketing'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'password'),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', '')
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# KAFKA CONSTANTS
TICKET_CREATION_TOPIC = os.environ.get('TICKET_CREATION_TOPIC', 'tickets')
TICKET_CREATION_MESSAGE_TYPE = os.environ.get(
    'TICKET_CREATION_MESSAGE_TYPE', 'tickets')
NEW_SALE_TOPIC = os.environ.get('NEW_SALE_TOPIC', 'sales')
NEW_SALE_MESSAGE_TYPE = os.environ.get('NEW_SALE_MESSAGE_TYPE', 'sales')
ACCOUNTING_SALE_TOPIC = os.environ.get('ACCOUNTING_SALE_TOPIC', 'acc_sales')
ACCOUNTING_SALE_MESSAGE_TYPE = os.environ.get(
    'ACCOUNTING_SALE_MESSAGE_TYPE', 'acc_sales')
