from django.urls import path
from .consumers import MessengerConsumer

ws_urlpatterns_messenger = [
	path('ws/notification/<str:room_name>/', MessengerConsumer.as_asgi())
]