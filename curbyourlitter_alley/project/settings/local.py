from .base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ADMINS = (
    ('Admin', 'admin@example.com'),
)

MANAGERS = ADMINS

MODERATORS = (
    'moderator@example.com',
)

TIME_ZONE = 'America/New_York'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, '../logs', 'django.log'),
            'maxBytes': 16777216, # 16megabytes
            'formatter': 'verbose'
        },
    },
    'root': {
        'handlers': ['log_file',],
        'level': 'DEBUG',
    },
}


#
# Django extensions
#

INSTALLED_APPS += (
    'django_extensions',
)


#
# debug toolbar settings
#

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# imagekit has to come after debug_toolbar else we get annoying templatetag
# errors
INSTALLED_APPS = tuple(filter(lambda a: a != 'imagekit', INSTALLED_APPS))

INSTALLED_APPS += (
    'debug_toolbar',
    'imagekit',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_ALLOW_ALL = True

BASE_URL = 'http://localhost:8000'
