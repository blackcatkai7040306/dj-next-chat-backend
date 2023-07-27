from rest_framework import serializers
from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    """
    Serializer for the chat model
    """
    class Meta:
        model = Chat
        fields = "__all__"
