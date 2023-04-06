from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class DjangoCronConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_cron'
    verbose_name = 'Django Cron'
