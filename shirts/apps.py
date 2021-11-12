from django.apps import AppConfig


class ShirtsConfig(AppConfig):
    name = 'shirts'

    def ready(self):
        # import signal handlers
        import shirts.signals

