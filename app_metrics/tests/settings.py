import os

import django

BASE_PATH = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

SITE_ID = 1

DEBUG = True

TEST_RUNNER = "djcelery.contrib.test_runner.CeleryTestSuiteRunner"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'djcelery',
    'app_metrics',
]

ROOT_URLCONF = 'app_metrics.tests.urls'

CELERY_ALWAYS_EAGER = True

APP_METRICS_BACKEND = 'app_metrics.backends.db'
APP_METRICS_MIXPANEL_TOKEN = None
APP_METRICS_DISABLED = False

SECRET_KEY = "herp-derp"
