from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser

@database_sync_to_async
def get_user_by_token(token_key):
    try:
        token = Token.objects.select_related('user').get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return None

class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        try:
            token_name, token_key = headers[b"authorization"].decode().split()
            if token_name == "Token":
                user = await get_user_by_token(token_key)
                if user:
                    scope["user"] = user
                else:
                    scope["user"] = AnonymousUser()
        except (KeyError, ValueError):
            scope["user"] = AnonymousUser()
        
        return await self.inner(scope, receive, send)
