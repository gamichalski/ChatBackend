from rest_framework.viewsets import ModelViewSet
from .serializers import HumanScienceAISerializer
from .models import HumanScienceAI
from django_filters.rest_framework import DjangoFilterBackend

class HumanScienceAIViewSet(ModelViewSet):
    queryset = HumanScienceAI.objects.all()
    serializer_class = HumanScienceAISerializer
    filter_backends = [DjangoFilterBackend]
    filter_backends = ('user', )