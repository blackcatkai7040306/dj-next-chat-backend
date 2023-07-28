import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from authentication.models import CustomUser

client = Client()


class CreateNewUserTest(TestCase):
    def setUp(self) -> None:
        self.valid_payload = {"username": "test_user1", "password": "TestUser@123"}
        self.invalid_payload = {"name": "test_user", "password": ""}

    def test_register_user(self) -> None:
        response = client.post(
            reverse("register_user"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self) -> None:
        response = client.post(
            reverse("register_user"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginUserTest(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create_user(
            username="test_user", password="TestUser@123"
        )
        self.valid_payload = {"username": "test_user", "password": "TestUser@123"}
        self.invalid_payload = {"username": "test_user", "password": "TestUser@1234"}

    def test_login_user(self) -> None:
        response = client.post(
            reverse("login_user"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid_user(self) -> None:
        response = client.post(
            reverse("login_user"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
