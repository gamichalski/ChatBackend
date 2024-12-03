from django.contrib import admin
from django.urls import path, include
from core.chatgptIA.views import GenericAIAVIewSet

from core.geminiIA.language.views import LanguageAIViewSet
from core.geminiIA.mathematics.views import MathAIViewSet

from core.authUser.views import UserViewSet
from core.chat.router import router as chat_router

from rest_framework.routers import DefaultRouter

from core.bias.views import ClassifyMessageView

router = DefaultRouter()
from core.authUser.views import UserViewSet
from core.geminiIA.language.views import LanguageAIViewSet
from core.geminiIA.mathematics.views import MathAIViewSet
from core.geminiIA.naturalscience.views import NaturalScienceAIViewSet
from core.geminiIA.humanscience.views import HumanScienceAIViewSet
from core.geminiIA.textwriting.views import TextWritingAIViewSet
from core.chat.views import AnswerViewSet

router.register("users", UserViewSet)
router.register("languageAI", LanguageAIViewSet)
router.register("mathAI", MathAIViewSet)
router.register("naturalscienceAI", NaturalScienceAIViewSet)
router.register("humanscienceAI", HumanScienceAIViewSet)
router.register("textwritingAI", TextWritingAIViewSet)
router.register("genericAI", GenericAIAVIewSet, basename="genericAI")
router.register("answers", AnswerViewSet)

from core.cohereIA.views import DatasetBIASViewSet, GenerateAndTrainModel, ClassifyTextView, CurrentCohereIAViewSet

router.register("dataset", DatasetBIASViewSet)
router.register("current-cohere-ia", CurrentCohereIAViewSet)

router.registry.extend(chat_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('generate-and-train/', GenerateAndTrainModel.as_view(), name='generate_and_train_model'),
    path('classify/', ClassifyTextView.as_view(), name='classify'),
    path("classify_message/", ClassifyMessageView.as_view(), name="classify_message"),
]
