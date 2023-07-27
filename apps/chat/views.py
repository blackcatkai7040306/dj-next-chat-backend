from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, APIException
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from chat.models import Chat
from chat.serializers import ChatSerializer


# Create your views here.


class ChatViewSet(ModelViewSet):
    """
    Perform CRUD operation on the chat model
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ChatSerializer

    def get_queryset(self):
        try:
            other_user = int(self.request.query_params.get("other_user"))
        except ValueError:
            raise ParseError("Invalid query params")
        except Exception:
            raise APIException("Some error occured")
        return (
            Chat.objects.filter(sender=self.request.user, receiver=other_user)
            | Chat.objects.filter(sender=other_user, receiver=self.request.user)
        ).order_by("created_date")

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "other_user",
                openapi.IN_QUERY,
                description="User id of the other user in the conversation",
                type=openapi.TYPE_INTEGER,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class UserChatView(ListAPIView):
    """
    Load chat list for the logged in user
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ChatSerializer

    def get_queryset(self):
        return (
            Chat.objects.filter(sender=self.request.user)
            | Chat.objects.filter(receiver=self.request.user)
        ).order_by("-created_date")
