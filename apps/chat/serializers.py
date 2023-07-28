from rest_framework import serializers
from authentication.serializers import UserSerializer
from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    """
    Serializer for the chat model
    """

    receiver_details = UserSerializer(read_only=True, source="receiver")
    sender_details = UserSerializer(read_only=True, source="sender")

    class Meta:
        model = Chat
        fields = (
            "message",
            "receiver",
            "created_date",
            "receiver_details",
            "sender_details",
        )

    def create(self, validated_data):
        validated_data["sender"] = self.context["request"].user
        return super().create(validated_data)
