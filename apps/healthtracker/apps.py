from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps.healthtracker'

    def ready(self):
        import apps.healthtracker.signals
