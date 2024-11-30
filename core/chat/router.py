from rest_framework.routers import DefaultRouter

from .views import ChatViewSet, AnswerViewSet

router = DefaultRouter()

router.register(r"chats", ChatViewSet)
