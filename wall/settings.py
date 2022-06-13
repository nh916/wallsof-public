from decouple import config
import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.template.context_processors import media

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# DOTENV_FILE = Path('.') / '.env'
# env_config = Config(RepositoryEnv(DOTENV_FILE))


SECRET_KEY = config('SECRET_KEY')
DEBUG = True
PRODUCTION_MODE = False

# if not PRODUCTION_MODE:
#     ALLOWED_HOSTS = []
# # ALLOWED_HOSTS = ['thewallsof.com']
# else:
#     ALLOWED_HOSTS = ['thewallsof.com', 'www.thewallsof.com', 'AugustusCaesar.pythonanywhere.com']

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wallOf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wall.wsgi.application'

#    sqlite database
sqlite_database = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# pgsql on docker
container_postgresql_database = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '12345678',
        'HOST': 'postgresql',
        'PORT': 5432,
    }
}

my_local_mysqlite_database = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thewallsof',
        'USER': 'root',
        'HOST': '127.0.0.1',

        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

DATABASES = sqlite_database

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_DIR = os.path.join(BASE_DIR, "Templates/static")

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

static_file = os.path.join(BASE_DIR, "templates/static")

STATICFILES_DIRS = [
    static_file
]

PARENT_BASE_DIR = Path(BASE_DIR).parent

MEDIA_URL = "/media/"

if PRODUCTION_MODE is False:
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
else:
    MEDIA_ROOT = os.path.join(PARENT_BASE_DIR, "media")
