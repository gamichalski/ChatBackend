from django.contrib import admin
from django.urls import path, include
from core.chatgptIA.views import GenericAIAVIewSet

from core.geminiIA.language.views import LanguageAIViewSet
from core.geminiIA.mathematics.views import MathAIViewSet


from rest_framework.routers import DefaultRouter


router = DefaultRouter()
from core.authUser.views import UserViewSet
from core.geminiIA.language.views import LanguageAIViewSet
from core.geminiIA.mathematics.views import MathAIViewSet
from core.geminiIA.naturalscience.views import NaturalScienceAIViewSet
from core.geminiIA.humanscience.views import HumanScienceAIViewSet
from core.geminiIA.textwriting.views import TextWritingAIViewSet

router.register("users", UserViewSet)
router.register("languageAI", LanguageAIViewSet)
router.register("mathAI", MathAIViewSet)
router.register("naturalscienceAI", NaturalScienceAIViewSet)
router.register("humanscienceAI", HumanScienceAIViewSet)
router.register("textwritingAI", TextWritingAIViewSet)
router.register("genericAI", GenericAIAVIewSet, basename="genericAI")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
