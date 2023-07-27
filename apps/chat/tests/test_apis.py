import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from authentication.models import CustomUser

client = Client()


class UserChatTest(TestCase):
    def setUp(self) -> None:
        self.user1 = CustomUser.objects.create_user(
            username="test_user1", password="TestUser@123"
        )
        self.user2 = CustomUser.objects.create_user(
            username="test_user2", password="TestUser@123"
        )
        self.valid_payload = {
            "message": "string",
            "sender": self.user1.id,
            "receiver": self.user2.id,
        }
        self.invalid_payload = {
            "message": "",
            "sender": self.user1.id,
            "receiver": self.user2.id,
        }

    def test_create_message(self) -> None:
        response = client.post(
            reverse("chat_view_set"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_message(self) -> None:
        response = client.post(
            reverse("chat_view_set"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_messages(self) -> None:
        response = client.get(
            reverse("chat_view_set"),
            {"sender": self.user1.id, "receiver": self.user2.id},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_messages(self) -> None:
        response = client.get(
            reverse("chat_view_set"),
            {"sender": "James", "receiver": self.user2.id},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
