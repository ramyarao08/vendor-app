"""
Django settings for mayan10 project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from __future__ import unicode_literals

import os
import sys

from django.utils.translation import ugettext_lazy as _

import mayan

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret_key_missing'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    # Placed at the top so it can override any template
    'appearance',
    # 3rd party
    'suit',
    # Django
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    # 3rd party
    'actstream',
    'autoadmin',
    'colorful',
    'compressor',
    'corsheaders',
    'djcelery',
    'formtools',
    'mathfilters',
    'mptt',
    'pure_pagination',
    'rest_framework',
    'rest_framework.authtoken',
    'solo',
    'stronghold',
    'widget_tweaks',
    # Base generic
    'acls',
    'authentication',
    'common',
    'converter',
    'django_gpg',
    'dynamic_search',
    'lock_manager',
    'mimetype',
    'navigation',
    'permissions',
    'smart_settings',
    'user_management',
    # Mayan EDMS
    'cabinets',
    'checkouts',
    'document_comments',
    'document_indexing',
    'document_parsing',
    'document_signatures',
    'document_states',
    'documents',
    'events',
    # Disable the folders app by default
    # Will be removed in the next version
    # 'folders',
    'linking',
    'mailer',
    'mayan_statistics',
    'metadata',
    'mirroring',
    'motd',
    'ocr',
    'rest_api',
    'sources',
    'storage',
    'tags',
    'task_manager',
    # Placed after rest_api to allow template overriding
    'rest_framework_swagger',
)

MIDDLEWARE_CLASSES = (
    'common.middleware.error_logging.ErrorLoggingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'common.middleware.timezone.TimezoneMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
    'common.middleware.ajax_redirect.AjaxRedirect',
)

ROOT_URLCONF = 'mayan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ]
        },
    },
]

WSGI_APPLICATION = 'mayan.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(MEDIA_ROOT, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# ------------ Custom settings section ----------

PROJECT_TITLE = mayan.__title__
PROJECT_WEBSITE = 'http://www.mayan-edms.com'
PROJECT_COPYRIGHT = mayan.__copyright__
PROJECT_LICENSE = mayan.__license__

LANGUAGES = (
    ('ar', _('Arabic')),
    ('bg', _('Bulgarian')),
    ('bs', _('Bosnian (Bosnia and Herzegovina)')),
    ('da', _('Danish')),
    ('de', _('German (Germany)')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fa', _('Persian')),
    ('fr', _('French')),
    ('hu', _('Hungarian')),
    ('hr', _('Croatian')),
    ('id', _('Indonesian')),
    ('it', _('Italian')),
    ('nl', _('Dutch (Netherlands)')),
    ('pl', _('Polish')),
    ('pt', _('Portuguese')),
    ('pt-br', _('Portuguese (Brazil)')),
    ('ro', _('Romanian (Romania)')),
    ('ru', _('Russian')),
    ('sl', _('Slovenian')),
    ('tr', _('Turkish')),
    ('vi', _('Vietnamese (Viet Nam)')),
    ('zh-cn', _('Chinese (China)')),
)

SITE_ID = 1

sys.path.append(os.path.join(BASE_DIR, 'apps'))

STATIC_ROOT = os.path.join(MEDIA_ROOT, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEST_RUNNER = 'common.tests.runner.MayanTestRunner'

# --------- Django compressor -------------
COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
)
COMPRESS_ENABLED = False
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
# --------- Django -------------------
LOGIN_URL = 'authentication:login_view'
LOGIN_REDIRECT_URL = 'common:home'
INTERNAL_IPS = ('127.0.0.1',)
# ---------- Django REST framework -----------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'PAGE_SIZE': 10,
}
# --------- Pagination --------
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 8,
    'MARGIN_PAGES_DISPLAYED': 2,
}
# ----------- Celery ----------
CELERY_ACCEPT_CONTENT = ('json',)
CELERY_ALWAYS_EAGER = True
CELERY_CREATE_MISSING_QUEUES = False
CELERY_DISABLE_RATE_LIMITS = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ENABLE_UTC = True
CELERY_QUEUES = []
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ROUTES = {}
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# ------------ CORS ------------
CORS_ORIGIN_ALLOW_ALL = True
# ------ Django REST Swagger -----
SWAGGER_SETTINGS = {
    'api_version': '1',
    'info': {
        'title': _('Mayan EDMS API Documentation'),
        'description': _('Free Open Source Document Management System.'),
        'contact': 'roberto.rosario@mayan-edms.com',
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html'
    }

}
# ------ Timezone --------
TIMEZONE_COOKIE_NAME = 'django_timezone'
TIMEZONE_SESSION_KEY = 'django_timezone'
# ----- Stronghold -------
STRONGHOLD_PUBLIC_URLS = (r'^/docs/.+$',)