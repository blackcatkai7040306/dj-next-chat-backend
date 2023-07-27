from django.test import TestCase
from authentication.models import CustomUser

# from faker import Faker


class UserTest(TestCase):
    """Test module for Puppy model"""

    def setUp(self) -> None:
        self.user1 = CustomUser.objects.create_user(
            username="test_user1", password="TestUser@123"
        )
        self.user2 = CustomUser.objects.create_user(
            username="test_user2", password="SecondTestUser@123"
        )

    def test_user(self) -> None:
        user_test_user_1 = CustomUser.objects.get(username="test_user1")
        user_test_user_2 = CustomUser.objects.get(username="test_user2")
        self.assertEqual(user_test_user_1.id, self.user1.id)
        self.assertEqual(user_test_user_2.id, self.user2.id)
