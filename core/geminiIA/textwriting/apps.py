from django.apps import AppConfig


class TextwritingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.geminiIA.textwriting'

    def ready(self):
        import core.geminiIA.textwriting.signal
