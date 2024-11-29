from rest_framework.serializers import ModelSerializer
from core.geminiIA.textwriting.models import TextWritingAI

class TextWritingAISerializer(ModelSerializer):
    class Meta:
        model = TextWritingAI
        fields: list[str] = ['id', 'user', 'answer', 'response', 'cover']