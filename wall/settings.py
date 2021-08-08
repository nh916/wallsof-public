import os
from pathlib import Path

from decouple import Config, RepositoryEnv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOTENV_FILE = Path('..') / '.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))

SECRET_KEY = env_config.get("SECRET_KEY")
DEBUG = env_config.get("DEBUG", cast=bool)

PRODUCTION_MODE = env_config.get("PRODUCTION_MODE", cast=bool)

if not PRODUCTION_MODE:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['thewallsof.com', 'www.thewallsof.com', 'AugustusCaesar.pythonanywhere.com']

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
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

#     psql Database
postgresql_database = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env_config.get("PSQL_NAME"),
        'USER': env_config.get("PSQL_USER"),
        'PASSWORD': env_config.get("PSQL_PASSWORD"),
        'HOST': env_config.get("PSQL_HOST"),
        'PORT': env_config.get("PSQL_PORT"),
    }
}

#    sqlite database
sqlite_database = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

my_local_mysqlite_database = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env_config.get("MYSQL_NAME"),
        'USER': env_config.get("MYSQL_USER"),
        'HOST': env_config.get("MYSQL_HOST"),
        # 'PORT': '3306',

        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

online_database = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env_config.get("PYTHON_ANYWHERE_MYSQL_NAME"),
        'USER': env_config.get("PYTHON_ANYWHERE_MYSQL_USER"),
        'PASSWORD': env_config.get("PYTHON_ANYWHERE_MYSQL_PASSWORD"),
        'HOST': env_config.get("PYTHON_ANYWHERE_MYSQL_HOST"),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


if not PRODUCTION_MODE:
    DATABASES = my_local_mysqlite_database
else:
    DATABASES = online_database

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
