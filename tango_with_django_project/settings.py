"""
Django settings for tango_with_django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#add template folders
TEMPLATE_PATH = os.path.join(BASE_DIR,'templates') #make absolute path from relative path
TEMPLATE_DIRS = (
                # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
                # Always use forward slashes, even on Windows.
                # Don't forget to use absolute paths, not relative paths.
                TEMPLATE_PATH,
                )

#add static path
STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/' # You may find this is already defined by default (see bottom).

STATICFILES_DIRS = (
    STATIC_PATH,
)

#add media path
# The first variable MEDIA_URL defines the base URL from which all media files will be accessible 
# on your development server. Setting the MEDIA_URL (for example) to /media/ will mean that user 
# uploaded files will be available from the URL http://127.0.0.1:8000/media/. 
# MEDIA_ROOT is used to tell Django where uploaded files should be stored on your local disk. 
# In here, we set this variable to the result of joining our PROJECT_PATH variable with /media/. 
# This gives an absolute path of <workspace>/tango_with_django_project/media/.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Absolute path to the media directory
#(Testing) try "http://127.0.0.1:8000/media/sample_upload.jpg" to see an image
#====================================================================
# WARNING: check The official Django documentation on static files, on
#          https://docs.djangoproject.com/en/1.7/ref/contrib/staticfiles/#static-file-development-view
#          before deployment!!!!!!!
#====================================================================
#LOGIN_URL = '/rango/login/' #ensures that the login_required() decorator will redirect any user not logged in to the URL /rango/login/
LOGIN_URL = '/accounts/login/'



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e9ul58@xbvs@yca#y!1u2^pmyfy#ozgo=h*b!s55mwundv+e3!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [] # Need to set this when deployment


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',
    'registration',
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

ROOT_URLCONF = 'tango_with_django_project.urls'

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'


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

#STATIC_URL = '/static/'

#for package 'django-registration-redux'
REGISTRATION_OPEN = True        # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/rango/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
                                # and are trying to access pages requiring authentication