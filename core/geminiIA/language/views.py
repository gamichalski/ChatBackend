from .serializers import LanguagesAISerializer
from .models import LanguagesAI
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class LanguageAIViewSet(ModelViewSet):
    queryset = LanguagesAI.objects.all()
    serializer_class = LanguagesAISerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user', )
