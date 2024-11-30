from django.apps import AppConfig


class GenericaiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.geminiIA.genericAI'
    
    def ready(self) -> None:
        import core.geminiIA.genericAI.signals
