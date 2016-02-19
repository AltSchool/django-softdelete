DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'my_db',
    }
}
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.eggs.Loader',
)


INSTALLED_APPS = [
    'softdelete',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'registration',
    'registration_defaults',
    'softdelete.test_softdelete_app',
]

DOMAIN = 'http://testserver'
ROOT_URLCONF = 'softdelete.urls'
SECRET_KEY = 'foo'

import os
import sys
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT))
