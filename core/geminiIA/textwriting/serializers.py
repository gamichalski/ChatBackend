from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.geminiIA.textwriting.models import TextWritingAI
from core.authUser.models import User

class TextWritingAISerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    class Meta:
        model = TextWritingAI
        fields: list[str] = ['id', 'user', 'answer', 'response', 'cover']