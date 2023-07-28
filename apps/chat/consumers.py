import json
import logging
from channels.consumer import AsyncConsumer

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncConsumer):
    """
    This is the consumer class for the chat app
    """
    def __init__(self) -> None:
        super().__init__()

    async def websocket_connect(self, event):
        user = self.scope["user"]
        self.userid = str(user.id)
        await self.channel_layer.group_add(self.userid, self.channel_name)
        await self.send({"type": "websocket.accept"})
        logger.info(
            "Connected to Socket: User id: %d, userrname: %d", user.id, user.username
        )

    async def websocket_receive(self, event):
        logger.info("Recieved event: %s", event)
        initial_data = event.get("text", None)

        await self.channel_layer.group_send(
            self.userid, {"type": "user_message", "text": initial_data}
        )

    async def user_message(self, event):
        logger.info("Send event: %s", event)
        await self.send({"type": "websocket.send", "text": json.dumps(event["text"])})

    async def websocket_disconnect(self, event):
        logger.info("Disconnected: %s", event)
