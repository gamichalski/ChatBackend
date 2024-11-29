from rest_framework.serializers import ModelSerializer
from core.chatgptIA.models import GenericAI

class GenericAISerializer(ModelSerializer):
    class Meta:
        model = GenericAI
        fields = "__all__"
        