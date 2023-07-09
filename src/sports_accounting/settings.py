"""
Django settings for sports_accounting project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

try:
    from . import local_settings
except ImportError:
    with open(BASE_DIR / 'sports_accounting/local_settings.py', 'w') as f:
        f.write('')
        raise ImportError(
            'local_settings.py was not found. The file has been created for you to added to your own settings. '
            '(You can refer to the README.md file for more information.)'
        )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = local_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = local_settings.DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'base_app',
    'main.apps.MainConfig',
    'member_module',
    'cash_module',
    'jazzmin',  # Must be before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django_cron',  # Should be at the end
    'main.apps.DjangoCronConfig',  # Same as above, but using this as it can provide a custom name for the app
    'rest_framework',
    'rest_framework_xml',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    # ),
    #
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sports_accounting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'sports_accounting.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': local_settings.DB_NAME,  # change this to your database name (inside local_settings.py)
        'USER': local_settings.DB_USER,  # change this to your username (inside local_settings.py)
        'PASSWORD': local_settings.DB_PASS,  # change this to your password (inside local_settings.py)
        'HOST': local_settings.DB_HOST,  # Or an IP Address that your DB is hosted on (inside local_settings.py)
        'PORT': local_settings.DB_PORT,  # change this port to your DB port (inside local_settings.py)
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
    'backup': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': local_settings.DB_BACKUP_USER,  # change this to your database name (inside local_settings.py)
        'PASSWORD': local_settings.DB_BACKUP_PASS,  # change this to your username (inside local_settings.py)
    }
}

# NoSQL DATABASE
MONGO_DB_URI = local_settings.MONGO_DB_URI
MONGO_DB_DATABASE = local_settings.MONGO_DB_DATABASE
MONGO_DB_CLUSTER = local_settings.MONGO_DB_CLUSTER

# Database backup settings (3rd party app - 'django-dbbackup')
# django-dbbackup: https://django-dbbackup.readthedocs.io/en/master/index.html
# Unfortunately, this 3rd party backup app works only on linux operating systems (production).

# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {
#     'location': BASE_DIR / 'backup',
#     # 'location': 'D:\\Nothing\\',
# }

# Cron jobs settings (3rd party app - 'django-cron') - will be used for backup
# django-cron: https://django-cron.readthedocs.io/en/latest/index.html
# To run cron jobs immediately, you need to run the following command: 'python manage.py runcrons'
CRON_CLASSES = [
    'main.cron.MongoDBBackupJob',
    'main.cron.MySQLDBBackupJob',
]

# Password hashing
# https://docs.djangoproject.com/en/4.1/topics/auth/passwords/

# Argon2 will be the default password hasher
# If you want to use a different hasher, you can change the order of the hashers below
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
# Media files (Images, Videos, etc. uploaded by users)
MEDIA_URL = 'media/'

# Static files folder
STATIC_ROOT = local_settings.STATIC_ROOT
# Media files folder
MEDIA_ROOT = local_settings.MEDIA_ROOT

# Static folders to be used
STATICFILES_DIRS = local_settings.STATICFILES_DIRS

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

# Define the session cookie age in seconds
SESSION_COOKIE_AGE = 60 * 60 * 24  # 1 day

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'main.User'

# Jazzmin settings (UI used in the admin panel)
JAZZMIN_SETTINGS = {
    'site_title': 'Sports Accounting',
    'site_header': 'Sports Accounting',
    'site_logo': 'assets/quintor-logo-square.png',
    'site_brand': 'Sports Accounting',
    "welcome_sign": "Sports Accounting Admin Login Page",
    "copyright": "Quintor",
    # "hide_apps": [
    #     "django_cron",
    # ],
    "order_with_respect_to": ["auth", "Main", "Main.User", ],
    "usermenu_links": [
        {"model": "auth.user"}
    ],
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Dashboard", "url": "admin:index"},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        {"name": "Reset Password", "url": "/admin/password_change/", "new_window": True},
        {"name": "Main page", "url": "/", "new_window": True},
    ],
    # Icons used for the admin apps (see https://fontawesome.com/v5/search)
    "icons": {
        "auth.Group": "fas fa-users",
        "main": "fas fa-users-cog",
        "main.User": "fas fa-user",
        "django_cron.CronJobLog": "fas fa-clock",
        "django_cron.CronJobLock": "fas fa-lock",
        "base_app.Transaction": "fas fa-file-invoice",
        "base_app.File": "fas fa-file",
        "base_app.Currency": "fas fa-euro-sign",
        "base_app.Category": "fas fa-list",
        "base_app.BalanceDetails": "fas fa-money-check-alt",
        "cash_module.CashTransaction": "fas fa-money-bill-wave",
        "member_module.Member": "fas fa-user-friends",
        "member_module.LinkedTransaction": "fas fa-link",
    },
    # Use modals instead of popups
    "related_modal_active": False,  # Some browsers will block modals (firefox)
    # Allows to edit UI in the admin panel (use only for development)
    "show_ui_builder": False,
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css":            "",
    # "custom_js":             "",
}
