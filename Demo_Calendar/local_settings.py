import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '%gt^83rk&=&5oy*!v_xrb51ffnk%7hwcbt!!bu^-n4l_at$8wc'
# use environmental file
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

DEBUG = True
