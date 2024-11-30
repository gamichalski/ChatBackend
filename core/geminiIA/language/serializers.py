from core.authUser.models import User
from .models import LanguagesAI
from rest_framework.serializers import ModelSerializer, SlugRelatedField

class LanguagesAISerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    class Meta:
        model = LanguagesAI
        fields: list[str] = ['id', 'user', 'answer', 'response', 'cover']
        