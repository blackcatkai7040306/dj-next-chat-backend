from django.urls import path
from rest_framework.routers import SimpleRouter
from chat.views import ChatViewSet


router = SimpleRouter()
router.register(r"chat-viewset", ChatViewSet, basename="chat")

urlpatterns = [
    path(
        "", ChatViewSet.as_view({"get": "list", "post": "create"}), name="chat_view_set"
    ),
]
