from rest_framework import serializers
from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    """
    Serializer for the chat model
    """
    class Meta:
        model = Chat
        fields = "__all__"
        extra_kwargs = {"sender": {"read_only": True}}

    def create(self, validated_data):
        validated_data["sender"] = self.context["request"].user
        return super().create(validated_data)

