from django.apps import AppConfig


class NaturalscienceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.geminiIA.naturalscience'

    def ready(self):
        import core.geminiIA.naturalscience.signal