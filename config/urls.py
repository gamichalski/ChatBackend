from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
from core.authUser.views import UserViewSet
from core.geminiIA.language.views import LanguageAIViewSet

router.register("users", UserViewSet)
router.register("languageAI", LanguageAIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
