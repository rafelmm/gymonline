# -*_ coding: utf-8 -*-

from .settings import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gymonlinedev',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
    )