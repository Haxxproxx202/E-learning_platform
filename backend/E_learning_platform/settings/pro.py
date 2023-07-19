from .base import *
import environ

env = environ.Env()
environ.Env.read_env()


DEBUG = False

ADMINS = (
    ('PMO', 'pjanecki88@gmail.com'),
)

ALLOWED_HOSTS = ['totututu.com', 'www.totututu.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        "PASSWORD": env('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
