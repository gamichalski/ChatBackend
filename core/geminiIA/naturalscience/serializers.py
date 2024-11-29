from rest_framework.serializers import ModelSerializer
from .models import NaturalScienceAI

class NaturalScienceAISerializer(ModelSerializer):
    class Meta:
        model = NaturalScienceAI
        fields: list[str] = ['id', 'user', 'answer', 'response']

        