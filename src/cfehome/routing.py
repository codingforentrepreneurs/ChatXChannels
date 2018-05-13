from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator


application = ProtocolTypeRouter({ 
    # Websocket chat handler
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                # url(r"chat/", ChatConsumer, name='chat')
                # url(r"chat/(?P<username>[\w.@+-]+)", ChatConsumer, name='chat')
                ]
            )
        ),
    )
})