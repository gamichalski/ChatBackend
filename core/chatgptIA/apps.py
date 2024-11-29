from django.apps import AppConfig


class AiMicrosserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.chatgptIA'
    
    def ready(self) -> None:
        import core.chatgptIA.signals