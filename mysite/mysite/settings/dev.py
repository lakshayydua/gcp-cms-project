from .base import *

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postrgresql', #did not work, so i changes to next line
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'qwerty1234',
        #'HOST': '127.0.0.1', # use gcp cloud sql hostname
        'HOST': '/cloudsql/gcp-project-253602:us-east1:gcp-project-postgres',
        #'PORT': '5432', # no need for port
    }

}
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'an insecure secret'

# SECURITY WARNING: define the correct hosts in production!
#ALLOWED_HOSTS = ['*']
# app engine gives up following host by default
ALLOWED_HOSTS = ['my-wagtail-project.appspot.com','127.0.0.1'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
