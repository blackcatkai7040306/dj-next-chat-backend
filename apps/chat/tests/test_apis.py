import json
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from authentication.models import CustomUser


class UserChatTest(APITestCase):
    def setUp(self) -> None:
        self.user1 = CustomUser.objects.create_user(
            username="test_user1", password="TestUser@123"
        )
        self.user2 = CustomUser.objects.create_user(
            username="test_user2", password="TestUser@123"
        )
        self.client.force_authenticate(self.user1)
        self.valid_payload = {
            "message": "string",
            "receiver": self.user2.id,
        }
        self.invalid_payload = {
            "message": "",
            "receiver": self.user2.id,
        }

    def test_create_message(self) -> None:
        response = self.client.post(
            reverse("post_chat"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_message(self) -> None:
        response = self.client.post(
            reverse("post_chat"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_messages(self) -> None:
        response = self.client.get(
            reverse("get_chat", kwargs={"userid": self.user2.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserConversationTest(APITestCase):
    def setUp(self) -> None:
        self.user1 = CustomUser.objects.create_user(
            username="test_user1", password="TestUser@123"
        )
        self.user2 = CustomUser.objects.create_user(
            username="test_user2", password="TestUser@123"
        )

    def test_get_conversations(self) -> None:
        self.client.force_authenticate(self.user1)
        response = self.client.get(reverse("user_chat"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_conversations_unauthorized(self) -> None:
        response = self.client.get(reverse("user_chat"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
