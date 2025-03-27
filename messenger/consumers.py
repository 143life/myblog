import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *

class MessengerConsumer(AsyncWebsocketConsumer):
	# Создание соединения фронта с сервером
	async def connect(self):
		self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
		await self.channel_layer.group_add(self.room_name, self.channel_name)
		await self.accept()
	
	# Разрыв соединения
	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(self.room_name, self.channel_name)

	# Получение сообщения от юзера и создание события с методом send_message
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json
		
		print(message)

		event = {
			'type': 'send_message',
			'message': message
		}

		await self.channel_layer.group_send(self.room_name, event)

	# Создание сообщения в БД и рассылка его всем подключенным юзерам
	async def send_message(self, event):
		data = event['message']
		# Сообщение добавляется в БД для каждого онлайн-пользователя, из-за чего происходят
		# дубликаты. Придумать, что с этим можно сделать.
		await self.create_message(data=data)
		response_data = {
			'sender': data['sender'],
			'message': data['message']
		}
		await self.send(text_data=json.dumps({'message': response_data}))

	# Метод специально для добавления в БД сообщения
	@database_sync_to_async
	def create_message(self, data):
		get_room_by_name = Room.objects.get(room_name=data['room_name'])
		new_message = Message(room=get_room_by_name, sender=data['sender'], message = data['message'])
		new_message.save()