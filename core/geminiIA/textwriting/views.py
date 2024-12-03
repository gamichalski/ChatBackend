from .models import TextWritingAI
from .serializers import TextWritingAISerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class TextWritingAIViewSet(ModelViewSet):
    queryset = TextWritingAI.objects.all()
    serializer_class = TextWritingAISerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user', )