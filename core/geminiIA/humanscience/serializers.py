from .models import HumanScienceAI
from rest_framework.serializers import ModelSerializer

class HumanScienceAISerializer(ModelSerializer):
    class Meta:
        model = HumanScienceAI
        fields: list[str] = ['id', 'user', 'response', 'answer', 'cover']