import os
from decouple import config, Csv
from os.path import join, dirname


DEBUG = config('DEBUG', cast=bool, default=False)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME", default="us-east-1")
AWS_S3_ENDPOINT_URL = config("AWS_S3_ENDPOINT_URL", default=None)
PIZZA_MODEL_BUCKET = config("PIZZA_MODEL_BUCKET")
AWS_DEFAULT_ACL = None
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='pizzatask'),
        'USER': config('DB_USER', default='pizzatask'),
        'PASSWORD': config('DB_PASSWORD', default='great_password'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': int(config('DB_PORT', default='5432'))
    }
}
SECRET_KEY = 'long_secret_password'
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "http://127.0.0.1:3000"]
CUSTOM_APPS = (
    'commands',
    'ingredients',
    'orders',
    'pizzas',
    'sizes',
    'users',
)
INSTALLED_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    *CUSTOM_APPS,
)
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
LOCALE_PATHS = [
    os.path.join(PROJECT_DIR, 'locale'),
]
ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app', 'statics', 'html'), ],
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
WSGI_APPLICATION = 'config.wsgi.application'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}][{asctime}][{module}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_DIR, 'debug.log'),
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console',],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = PROJECT_DIR + "media"
MEDIA_URL = '/'
STATIC_URL = config('STATIC_URL', default='/statics/')
STATIC_ROOT = os.path.join(PROJECT_DIR, "statics/")
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
if DEBUG:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'app', 'statics'),)
