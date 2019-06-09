from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'myauth'

    def ready(self):
        from . import signals