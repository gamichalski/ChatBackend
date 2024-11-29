from rest_framework.viewsets import ModelViewSet
from core.chatgptIA.serializer import GenericAISerializer
from core.chatgptIA.models import GenericAI
from django_filters.rest_framework import DjangoFilterBackend

class GenericAIAVIewSet(ModelViewSet):
    queryset = GenericAI.objects.all()
    serializer_class = GenericAISerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user', )