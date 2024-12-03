from django.apps import AppConfig

class MathematicsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.geminiIA.mathematics'

    def ready(self):
        import core.geminiIA.mathematics.signal