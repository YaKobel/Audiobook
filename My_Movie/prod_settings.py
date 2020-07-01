import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'jjycfpu45p#zi-6329(j2dwd1dsfvgbd67544sveda%mp7ezke*_@ar4i'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movie',
        'USER': 'postgres',
        'PASSWORD': 'G21009',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')