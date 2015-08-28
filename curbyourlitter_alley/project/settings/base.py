import os
from os.path import abspath, dirname

from django.core.exceptions import ImproperlyConfigured

PROJECT_ROOT = os.path.join(abspath(dirname(__file__)), '..', '..')


ENV_VARIABLE_PREFIX = 'CYL'

def get_env_variable(var_name):
    """Get the environment variable or return exception"""
    if not ENV_VARIABLE_PREFIX:
        raise ImproperlyConfigured('Set ENV_VARIABLE_PREFIX')
    try:
        return os.environ[ENV_VARIABLE_PREFIX + '_' + var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cartodbsync',
    'corsheaders',
    'rest_framework',
    'rest_framework_gis',

    'canrequests',
    'socratasync',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, '..', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': get_env_variable('DB_HOST'),
        'PORT': get_env_variable('DB_PORT'),
    }
}


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Media and static paths
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '..', 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, '..', 'collected_static')
STATIC_URL = '/static/'

EMAIL_SUBJECT_PREFIX = '[Curb Your Litter] '

SECRET_KEY = get_env_variable('SECRET_KEY')

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding',
    'cache-control',
)

CARTODB_SYNC = {
    'API_KEY': get_env_variable('CARTODBSYNC_API_KEY'),
    'DOMAIN': get_env_variable('CARTODBSYNC_DOMAIN'),
    'MODELS': [
        {
            'CARTODB_TABLE': get_env_variable('CARTODBSYNC_CANREQUEST_TABLE'),
            'MODEL_CLASS': 'canrequests.CanRequest',
            'SYNCHRONIZER_CLASS': 'canrequests.cartodbsynchronizers.CanRequestSynchronizer',
        }
    ]
}
