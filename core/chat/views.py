from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Chat, ChatMessage
from .serializers import ChatSerializer, ChatMessageSerializer

# Create your views here.
class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatMessageViewSet(ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer