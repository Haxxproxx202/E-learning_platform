from .base import *
import environ

env = environ.Env()
environ.Env.read_env()


DEBUG = False

ADMINS = (
    ('PMO', 'pjanecki88@gmail.com')
)

ALLOWED_HOSTS = ['edu.com', 'www.edu.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        "PASSWORD": env('DATABASE_PASSWORD')
    }
}
