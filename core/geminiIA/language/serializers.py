from core.geminiIA.language.models import LanguagesAI
from rest_framework.serializers import ModelSerializer

class LanguagesAISerializer(ModelSerializer):
    class Meta:
        model = LanguagesAI
        fields: list[str] = ['id', 'user', 'answer', 'response', 'cover']
        