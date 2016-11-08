from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "interface_platform"

    def ready(self):
        import_module("interface_platform.receivers")
