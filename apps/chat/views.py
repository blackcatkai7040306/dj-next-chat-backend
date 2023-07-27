from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from chat.models import Chat
from chat.serializers import ChatSerializer


# Create your views here.


class ChatViewSet(ModelViewSet):
    """
    Perform CRUD operation on the chat model
    """

    permission_classes = (AllowAny,)
    serializer_class = ChatSerializer

    def get_queryset(self):
        try:
            sender = int(self.request.query_params.get("sender"))
            receiver = int(self.request.query_params.get("receiver"))
        except ValueError:
            raise ParseError("Invalid query params")
        return (
            Chat.objects.filter(sender=sender, receiver=receiver)
            | Chat.objects.filter(sender=receiver, receiver=sender)
        ).order_by("created_date")

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "sender",
                openapi.IN_QUERY,
                description="User id of the Sender",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "receiver",
                openapi.IN_QUERY,
                description="User id of Receiver",
                type=openapi.TYPE_INTEGER,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
