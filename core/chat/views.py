from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Chat, Answer
from .serializers import ChatSerializer, AnswerSerializer
from django_filters.rest_framework import DjangoFilterBackend


import django_filters
from .models import Answer

class AnswerFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name="chat__user__id")

    class Meta:
        model = Answer
        fields = ['user_id']

class AnswerFilterChat(django_filters.FilterSet):
    chat_id = django_filters.NumberFilter(field_name="chat__id")

    class Meta:
        model = Answer
        fields = ['chat_id']


class ChatFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name="user__id")

    class Meta:
        model = Chat
        fields = ['user_id']


class ChatViewSet(ModelViewSet):

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChatFilter

class AnswerFilter(django_filters.FilterSet):
    chat_id = django_filters.NumberFilter(field_name="chat__id")
    user_id = django_filters.NumberFilter(field_name="chat__user__id")

    class Meta:
        model = Answer
        fields = ['chat_id', 'user_id']


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnswerFilter
