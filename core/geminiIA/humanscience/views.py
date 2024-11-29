from rest_framework.viewsets import ModelViewSet
from core.geminiIA.humanscience.serializers import HumanScienceAISerializer
from core.geminiIA.humanscience.models import HumanScienceAI
from django_filters.rest_framework import DjangoFilterBackend

class HumanScienceAIViewSet(ModelViewSet):
    queryset = HumanScienceAI.objects.all()
    serializer_class = HumanScienceAISerializer
   