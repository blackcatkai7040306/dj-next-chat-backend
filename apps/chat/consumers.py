import json
from channels.consumer import AsyncConsumer




class ChatConsumer(AsyncConsumer):
    def __init__(self) -> None:
        super().__init__()
    
    async def websocket_connect(self, event):
        print("connected", event)
        user = self.scope["user"]
        self.userid = str(user.id)
        await self.channel_layer.group_add(self.userid, self.channel_name)
        await self.send({"type": "websocket.accept"})
       

    async def websocket_receive(self, event):
        print("receive", event)
        initial_data = event.get("text", None)

        await self.channel_layer.group_send(
            self.userid, {"type": "user_message", "text": initial_data}
        )

    async def user_message(self, event):
        print("send", event)
        await self.send({"type": "websocket.send", "text": json.dumps(event["text"])})

    async def websocket_disconnect(self, event):
        print("disconnected", event)
