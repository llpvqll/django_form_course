from django.apps import AppConfig


class OrmLessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orm_less'
