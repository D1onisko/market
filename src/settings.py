# -*- coding: utf-8 -*-
import os
import sys
import glob

SECRET_KEY = 'u!n*1uz-5dz(ec2fbux4(z1g@7ccb@!2fmcmqx^izlk^zml%!q'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
SITE_ID = 1
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

def rel_project(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)


def REL(*x):
    return rel_project(*x)

rel_public = lambda *x: rel_project('static', *x)
sys.path.insert(0, rel_project('..', 'lib'))
gettext_noop = lambda s: s

THUBMNAIL_DUBUG = True
# +++++++++++++++++++++++++  Application definition +++++++++++++++++++
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/portal'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}
INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    'haystack',
    'annoying',
    'sorl.thumbnail',
    'registration',


    'src.user_profile',
    'src.core',
    'src.shop',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

)

ROOT_URLCONF = 'src.urls'
WSGI_APPLICATION = 'src.wsgi.application'


# ++++++++++++++++++++++++++++++  Database  +++++++++++++++++++++++++++
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'market',
        'USER': 'root',
        'PASSWORD': 'ahillessd1',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '',
    }
}
# ++++++++++++++++++++++++++++++   Internationalization ++++++++++++++++
RECAPTCHA_PUBLIC = ''
RECAPTCHA_PRIVATE = ''
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ++++++++++++++++++++++++++++++++ Static files (CSS, JavaScript, Images) +++++++++++++++++++++++++++++
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',

)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    rel_project('templates'),
)

MEDIA_ROOT = rel_public('media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel_public('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    rel_project('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#+++++++++++++++++++++++++++++++++++  Mail ++++++++++++++++++++++++++++++++++++

ACCOUNT_ACTIVATION_DAYS = 2

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'info@google.ru'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = (os.path.join(os.path.dirname(__file__), '../mail'))
