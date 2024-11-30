from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Chat, Answer
from .serializers import ChatSerializer, AnswerSerializer

# Create your views here.
class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer