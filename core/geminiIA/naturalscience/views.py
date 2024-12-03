from rest_framework.viewsets import ModelViewSet
from .serializers import NaturalScienceAISerializer
from .models import NaturalScienceAI
from django_filters.rest_framework import DjangoFilterBackend

class NaturalScienceAIViewSet(ModelViewSet):
    queryset = NaturalScienceAI.objects.all()
    serializer_class = NaturalScienceAISerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user', )