"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _

# from django.conf.global_settings import STATICFILES_DIRS
from tests.test_settings import CRISPY_ALLOWED_TEMPLATE_PACKS, CRISPY_TEMPLATE_PACK

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vxo$^26%q9tq1$erg@yoe-1y&&m!_q+5)uyvt*+tlmu*@$a*8#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition

INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
  "tailwind",
  "theme",
  "crispy_forms",
  "crispy_tailwind",
  "django_browser_reload",
  "cart.apps.CartConfig",
  "shop.apps.ShopConfig",
  "orders.apps.OrdersConfig",
  "payment.apps.PaymentConfig",
  "coupons.apps.CouponsConfig",
  'rosetta',
  'parler',
  'localflavor',
]

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.middleware.locale.LocaleMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
  "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": ["templates/"],
    "APP_DIRS": True,
    "OPTIONS": {
      "context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
        "cart.context_processors.cart",
      ],
    },
  },
]

WSGI_APPLICATION = "project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
  }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
  },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"
LANGUAGES = [
  ('en', _('English')),
  ("ru", _("Russian")),
]
LOCALE_PATHS = [
  BASE_DIR / 'locale',
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
'''##########################################################################'''
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
  "127.0.0.1",
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [BASE_DIR / 'main_staticfiles/']

CART_SESSION_ID = 'cart'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'

STRIPE_PUBLISHABLE_KEY = 'pk_test_51ORmcgKakDnB0h0kJeZaWbWgqJ7hf9t4wsvqZgLcIEjbWhbbylirabAUnFXwwzmxQZcHWf3mmQSI4Wel78kQqhIt00vRB90dUb'
STRIPE_SECRET_KEY = 'sk_test_51ORmcgKakDnB0h0kZsQh4APuMNqL0aLwGzjWH7RwiK85zdYzBfon2pcxPHz1heGSUztBCUQiPLwQWS7v6ED1dErV00BscdUafl'
# STRIPE_API_VERSION = '2022-08-01'
STRIPE_API_VERSION = '2023-10-16'
STRIPE_WEBHOOK_SECRET = 'whsec_cea21d5c4967e18f46ff896dc7f067be660349eb21ef6701763b1a0a1fe79f17'

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = "static/"

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

# * django-parler's settings
PARLER_DEFAULT_LANGUAGE_CODE = 'en'

PARLER_LANGUAGES = {
  None: ({
    'code': 'en',
  }, {
    'code': 'ru',
  }),
  'default': {
    'fallbacks': ['en'],
    'hide_untranslated': False,
  }
}
