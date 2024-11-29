from rest_framework import serializers

from .models import Chat, ChatMessage
from core.authUser.serializers import UserSerializer

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["chat_name", "ia", "user"]
        depth = 2

class ChatMessageSerializer(serializers.ModelSerializer):
    author = UserSerializer()  # Se o author for um User, use o UserSerializer

    class Meta:
        model = ChatMessage
        fields = ["author_type", "body", "timestamp", "chat", "author"]
        depth = 2
