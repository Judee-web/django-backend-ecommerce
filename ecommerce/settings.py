"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import cloudinary
import cloudinary.uploader
import cloudinary.api
from pathlib import Path
from datetime import timedelta
import os
import stripe

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



STRIPE_API_KEY = os.environ.get('sk_test_51N4C2MCnAe4mWFw2TKo8V3gkpZAfU7YE7oJF0MAJUZakxSOjm6jXC01q2knSLXfNI0moAvwoSF9Vhm9setmKAqJ400kB90PKWO')
STRIPE_API_SECRET = os.environ.get('pk_test_51N4C2MCnAe4mWFw2fLdkdIxaFOibNbuLjEBZRWOUmLEXyK68JmvmAr5aKhisWfsiaXaZTzz6z6uysSrNeAWwCsf1001cwsuWQq')
stripe.api_key='sk_test_51N4C2MCnAe4mWFw2TKo8V3gkpZAfU7YE7oJF0MAJUZakxSOjm6jXC01q2knSLXfNI0moAvwoSF9Vhm9setmKAqJ400kB90PKWO'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!c%inbqkwpe8%%nh)tgh#9s%a^5ii(y#93konzt52t&$9=&ur0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
        'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'products',
    'users',
    'cart',
    'wishlist',
    'orders',
    'rest_framework',
    'corsheaders',
    'django_filters',


]

AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
     'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    
]


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:3000',
#     'http://localhost',
#     'https://localhost:3000',
#     'http://localservername',
#      'http://127.0.0.1:3000',
#     'http://localservername',
#     'https://checkout.stripe.com',
    
# )
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS=[
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    
]
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'https://checkout.stripe.com',
    'https://checkout.stripe.com'
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    'http://localhost:3000',
]
CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]


SITE_URL = 'http://localhost:3000'
ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://django_ecommerce_2vyf_user:koMRfgt7wrUtY2vhrgDNuKGuzTOdLw8A@dpg-cud4m31opnds73apolr0-a/django_ecommerce_2vyf',
        conn_max_age=600  # Optional, for persistent database connections
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# STATICFILES_DIRS = [
#     '../static',
# ]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

cloudinary.config(
  cloud_name = "ddk98mjzn",
  api_key = "645519149712985",
  api_secret = "A_bL776CwLO54Elq8AoeyTLBlmM"
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "SIGNING_KEY": 'somesecretsecretsomekeysecret',
}



STRIPE_SECRET_WEBHOOK='whsec_03ce6b586620eec93594579b709130478dcfcaad93cfd2cf2f75f64f10d6c397'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
JAZZMIN_SETTINGS = {
    "site_title": "E-Commerce Dashboard",
    
    "site_header": "E-Commerce Dashboard",
    
        "site_brand": "E-Commerce Admin",

    "login_logo": 'images.png',
    "site_logo": "images.png",
    
    "welcome_sign": "Welcome to the e-commerce Dashboard ITI",

    "copyright": "e-commerce Dashboard ITI",
    
        "search_model": ["auth.User", "auth.Group"],
        
        
      "topmenu_links": [

        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        {"model": "auth.User"},

        {"app": "books"},
    ],




    
}