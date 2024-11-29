from rest_framework.serializers import ModelSerializer
from .models import MathAI

class MathAISerializer(ModelSerializer):
    class Meta:
        model = MathAI
        fields: list[str] = ['id', 'user', 'answer', 'response', 'cover']