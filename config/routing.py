from django.urls.conf import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from chat.consumers import ChatConsumer


application = ProtocolTypeRouter(
    {
        "websocket": OriginValidator(
            URLRouter([path("ws/<str:userid>/", ChatConsumer.as_asgi())]),
            ["*"],
        )
    }
)
