from django.urls import path
from rest_framework.routers import SimpleRouter
from chat.views import ChatViewSet, UserConversations


router = SimpleRouter()
router.register(r"chat-viewset", ChatViewSet, basename="chat")

urlpatterns = [
    path("messages/", ChatViewSet.as_view({"post": "create"}), name="chat_view_set"),
    path(
        "messages/<int:userid>",
        ChatViewSet.as_view({"get": "list"}),
        name="chat_view_set",
    ),
    path("conversations/", UserConversations.as_view(), name="user_chat"),
]
