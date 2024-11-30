from core.authUser.models import User
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import MathAI

class MathAISerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    class Meta:
        model = MathAI
        fields: list[str] = ['id', 'user', 'answer', 'response', 'cover']