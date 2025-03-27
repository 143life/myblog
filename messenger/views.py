from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import *

class RoomView(View):
	def get(self, request):
		return render(request, 'messenger/index.html')
	# переход в указанную комнату
	def post(self, request):
		username = request.POST['username']
		room = request.POST['room']
		try:
			get_room = Room.objects.get(room_name=room)
		except Room.DoesNotExist:
			new_room = Room(room_name=room)
			new_room.save()
		return redirect('room', room_name=room, username=username)

class MessageView(View):
	def get(self, request, room_name, username):
		# найти нужную комнату
		room = Room.objects.get(room_name=room_name)
		# использовать найденную комнату, чтобы найти все ее сообщения
		messages = Message.objects.filter(room=room)
		context = {
			"messages": messages,
			"user": username,
			"room_name": room_name
		}
		return render(request, 'messenger/message.html', context)
	#def post(self, )
	