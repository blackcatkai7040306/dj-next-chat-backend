from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
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
        receiver = validated_data.get("receiver")
        message_obj = {
            "message": validated_data.get("message"),
            "sender_id": validated_data.get("sender").id,
            "sender_username": validated_data.get("sender").username,
        }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            group=str(receiver.id),
            message={
                "type": "user_message",
                "text": message_obj,
            },
        )

        return super().create(validated_data)
