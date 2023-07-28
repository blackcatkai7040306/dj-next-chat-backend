from rest_framework import serializers
from authentication.models import CustomUser
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "id")

class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = CustomUser
        fields = ("username", "password", "token")
        extra_kwargs = {
            "username": {"write_only": True},
            "password": {"write_only": True},
            "token": {"read_only": True},
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data.get("username"),
        )
        user.set_password(validated_data.get("password"))
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        return user
