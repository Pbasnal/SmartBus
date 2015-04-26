#Embedded file name: /home/basnal/DRT/SmartBus/SmartBus/settings.py
"""
Django settings for SmartBus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '252w067$s!4d7^@%$z=%(v*rbgw5#df_r4g#hs^$-8-dvyrj@@'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = ('django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'DRT')

MIDDLEWARE_CLASSES = ('django.contrib.sessions.middleware.SessionMiddleware',
                      'django.middleware.common.CommonMiddleware',
                      'django.middleware.csrf.CsrfViewMiddleware',
                      'django.contrib.auth.middleware.AuthenticationMiddleware',
                      'django.contrib.messages.middleware.MessageMiddleware',
                      'django.middleware.clickjacking.XFrameOptionsMiddleware')

ROOT_URLCONF = 'SmartBus.urls'
WSGI_APPLICATION = 'SmartBus.wsgi.application'

DATABASES = {
    'default': {   'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    },
    'mongo' : {
      'ENGINE' : 'django_mongodb_engine',
      'NAME' : 'drtdb'
   }
}

NEO4J_DATABASES = {
    'default' : {
        'HOST':'localhost',
        'PORT':7474,
        'ENDPOINT':'/db/data'
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
