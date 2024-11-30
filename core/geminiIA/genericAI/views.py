from rest_framework.viewsets import ModelViewSet
from core.geminiIA.genericAI.models import GeminiGenericAi
from core.geminiIA.genericAI.serializer import GeminiGenericAiSerializer
from django_filters.rest_framework import DjangoFilterBackend

class GenericGeminiAIViewSet(ModelViewSet):
    queryset = GeminiGenericAi.objects.all()
    serializer_class = GeminiGenericAiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user', )