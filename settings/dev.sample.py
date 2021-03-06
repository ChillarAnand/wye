# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "wye",
        'USER': "",
        'PASSWORD': "",
        'HOST': "localhost",
        'PORT': "5432",
    }
}

# E-Mail Settings
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
