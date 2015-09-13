# -*_ coding: utf-8 -*-

from .settings import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': django_secret_key.DB_NAME['test'],
        'USER': django_secret_key.DB_USER,
        'PASSWORD': django_secret_key.DB_PASSWORD,
    }
}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
    )

SITE_ID = 1