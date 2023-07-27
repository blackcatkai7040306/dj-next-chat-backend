from django.db import models
from common.models import TimeStampedModel


# Create your models here.
class Chat(TimeStampedModel):
    """
    Models for storing chat messages
    """

    message = models.CharField(max_length=511)
    sender = models.ForeignKey(
        "authentication.CustomUser", on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        "authentication.CustomUser", on_delete=models.CASCADE, related_name="receiver"
    )

    def __str__(self) -> str:
        return str(self.message)
