from core.geminiIA.mathematics.serializers import MathAISerializer
from core.geminiIA.mathematics.models import MathAI
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class MathAIViewSet(ModelViewSet):
    queryset = MathAI.objects.all()
    serializer_class = MathAISerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user', )