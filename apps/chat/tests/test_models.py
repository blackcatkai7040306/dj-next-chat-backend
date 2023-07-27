from django.test import TestCase
from chat.models import Chat
from authentication.models import CustomUser

# from faker import Faker


class UserTest(TestCase):
    """Test module for user model"""

    def setUp(self) -> None:
        self.user1 = CustomUser.objects.create(
            username="test_user1", password="TestUser@123"
        )
        self.user2 = CustomUser.objects.create_user(
            username="test_user2", password="SecondTestUser@123"
        )
        self.chat1 = Chat.objects.create(message="Hello", sender=self.user1, receiver=self.user2)
        self.chat2 = Chat.objects.create(message="Hi", sender=self.user2, receiver=self.user1)

    def test_chat(self) -> None:
        chat_obj1 = Chat.objects.filter(sender=self.user1).first()
        chat_obj2 = Chat.objects.filter(sender=self.user2).first()
        self.assertEqual(chat_obj1, self.chat1)
        self.assertEqual(chat_obj2, self.chat2)
