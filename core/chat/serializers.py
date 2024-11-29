from rest_framework import serializers

from .models import Chat, ChatMessage

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["chat_name", "ia", "user"]

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ["author_type", "body", "timestamp", "chat", "author"]
