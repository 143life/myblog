"""
ASGI config for myblog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter

from chat.routing import ws_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

#application = get_asgi_application()
application = ProtocolTypeRouter({
	'http': get_asgi_application(),
	'websocket': AuthMiddlewareStack(
		URLRouter(ws_urlpatterns)
	)
})
