from base import *

LOCAL_SETTINGS_LOADED = True

DEBUG = True

INTERNAL_IPS = ('127.0.0.1', )

ADMINS = (
    ('Your Name', 'username@example.com'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mallzaad',
        'USER':  'mallzaad',
        'PASSWORD': 'zaadpassword',
        'HOST': 'localhost',
        'PORT': '',

    }
}
