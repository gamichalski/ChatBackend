from django.apps import AppConfig

class HumanscienceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.geminiIA.humanscience'

    def ready(self):
        import core.geminiIA.humanscience.signal
