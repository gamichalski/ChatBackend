from rest_framework.serializers import ModelSerializer
from core.geminiIA.genericAI.models import GeminiGenericAi

class GeminiGenericAiSerializer(ModelSerializer):
    class Meta:
        model = GeminiGenericAi
        fields = "__all__"