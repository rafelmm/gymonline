# -*_ coding: utf-8 -*-

from .settings import *

DEBUG = True
TEMPLATES[0]['TEMPLATE_DEBUG'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev_db.sqlite3'),
    }
}
