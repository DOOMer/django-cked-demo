"""
Django settings for django_cked_demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^4rs!gk--icpt_sfxo+(d-21*tlbs33k!xb6s#7ukz)f%(se=='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


from django.contrib.admin.sites import AdminSite

SITE_TITLE = "django-cked demo"
AdminSite.site_header = SITE_TITLE
AdminSite.site_title = SITE_TITLE
AdminSite.index_title = "Administration " + AdminSite.site_title


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cked',
    'django_cked_demo.cked_demo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_cked_demo.urls'

WSGI_APPLICATION = 'django_cked_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media/')

# elFinder config. See https://github.com/Studio-42/elFinder/wiki/Client-configuration-options
ELFINDER_OPTIONS = {
    ## required options
    'root': os.path.join(MEDIA_ROOT,  'images'),
    'URL': '/media/images/',
}

# CKEditor config. See http://docs.ckeditor.com/#!/guide/dev_configuration
CKEDITOR_OPTIONS = {
    'skin': 'moono',
    'toolbar': [
            [
            '-', 'Bold', 'Italic', 'Underline', 'Strike',
            '-', 'BulletedList', 'NumberedList',
            '-','Blockquote','-','JustifyLeft','JustifyCenter','JustifyRight',
            '-', 'Image', 'Link', 'Unlink', 'Anchor', 'HorizontalRule',
            '-', 'Source','Undo', 'Redo',
            ],
        ],
    'filebrowserWindowWidth': 940,
    'filebrowserWindowHeight': 450,
    'width': 900,
    'height': 480,
}