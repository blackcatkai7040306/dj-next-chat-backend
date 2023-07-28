from django.urls.conf import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from chat.consumers import ChatConsumer
from config.middleware import TokenAuthMiddleware


application = ProtocolTypeRouter(
    {
        "websocket": OriginValidator(
            TokenAuthMiddleware(
                URLRouter([path("ws/", ChatConsumer.as_asgi())])
            ),
            ["*"],
        )
    }
)
