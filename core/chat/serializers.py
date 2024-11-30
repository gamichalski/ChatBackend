from rest_framework import serializers

from .models import Chat, Answer
from core.authUser.serializers import UserSerializer

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["id","chat_name", "ia", "user"]
        depth = 2

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"
        depth = 2
