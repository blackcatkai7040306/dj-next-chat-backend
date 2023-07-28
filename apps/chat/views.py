from django.db.models import F, Func, Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, APIException
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
            userid = int(self.kwargs.get("userid"))
        except ValueError:
            raise ParseError("Invalid query params")
        except Exception:
            raise APIException("Some error occured")
        return (
            Chat.objects.filter(sender=self.request.user, receiver=userid)
            | Chat.objects.filter(sender=userid, receiver=self.request.user)
        ).order_by("created_date")




class UserConversations(ListAPIView):
    """
    Load chat list for the logged in user
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ChatSerializer

    def get_queryset(self):
        return (
            Chat.objects.filter(
                Q(sender=self.request.user) | Q(receiver=self.request.user)
            ).order_by("-created_date")
            .annotate(
                greatest_user=Func(F("sender"), F("receiver"), function="GREATEST"),
                least_user=Func(F("sender"), F("receiver"), function="LEAST"),
            )
            .order_by("greatest_user", "least_user")
            .distinct("greatest_user", "least_user")
        )
