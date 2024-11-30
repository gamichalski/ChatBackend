from core.authUser.models import User
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import NaturalScienceAI

class NaturalScienceAISerializer(ModelSerializer):
    class Meta:
        model = NaturalScienceAI
        fields: list[str] = ['id', 'user', 'answer', 'response', 'cover']

