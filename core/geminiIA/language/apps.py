from django.apps import AppConfig


class LanguageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.geminiIA.language' 

    def ready(self):
        import core.geminiIA.language.signal
    
