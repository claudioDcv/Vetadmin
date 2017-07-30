from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'apps.core'
    verbose_name = 'núcleo'

    def ready(self):
        import apps.core.signals # noqa
