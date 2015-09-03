# -*_ coding: utf-8 -*-

from .settings import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gymonlinetest',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
