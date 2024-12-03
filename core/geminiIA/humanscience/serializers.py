from .models import HumanScienceAI
from core.authUser.models import User
from rest_framework.serializers import ModelSerializer, SlugRelatedField

class HumanScienceAISerializer(ModelSerializer):
    class Meta:
        model = HumanScienceAI
        fields: list[str] = ['id', 'user', 'response', 'answer', 'cover']