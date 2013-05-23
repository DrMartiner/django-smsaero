import sys
import os.path

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
sys.path.insert(0, ROOT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SMSAERO_USER = ''
SMSAERO_PASSWORD = ''
SMSAERO_PASSWORD_MD5 = ''

SECRET_KEY = '!!!very_secret!!!'
ROOT_URLCONF = 'smsaero.urls'
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'factory',
    'smsaero',
)