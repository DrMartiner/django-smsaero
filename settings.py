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

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '',
    },
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
    'django_rq',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        }
    },
    'handlers': {
        'sms_send': {
                'level': 'DEBUG',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': os.path.join(ROOT, 'sms_send.log'),
                'formatter': 'verbose'
            }
    },
    'loggers': {
        'smsaero': {
            'handlers': ['sms_send'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}










