from rest_framework.serializers import ModelSerializer
from core.geminiIA.naturalscience.models import NaturalScienceAI

class NaturalScienceAISerializer(ModelSerializer):
    class Meta:
        model = NaturalScienceAI
        fields: list[str] = ['id', 'user', 'answer', 'response', 'cover']

