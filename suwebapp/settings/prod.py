# ALL SETTINGS WHICH ONLY NEEDED FOR PRODUCTION ENVIRONMENT

import dj_database_url
from django.conf import settings


DEBUG = False
TEMPLATE_DEBUG = True


db_from_env = dj_database_url.config()

DATABASES = settings.DATABASES

DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# DEBUG_COLLECTSTATIC=1
DISABLE_COLLECTSTATIC=1
