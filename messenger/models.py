from django.db import models

# 4. Создать модели

class Room(models.Model):
	room_name = models.CharField('Название комнаты',max_length=255)

	def __str__(self):
		return self.room_name
	# класс Meta содержит внетабличные данные о таблице(имя, удобочитаемые имена, и тд)
	class Meta:
		verbose_name = "Комната"
		verbose_name_plural = "Комнаты"
	
class Message(models.Model):
	room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната')
	sender = models.CharField('Отправитель', max_length=255)
	message = models.TextField('Сообщение')

	def __str__(self):
		return str(self.room)
	
	class Meta:
		verbose_name = "Сообщение"
		verbose_name_plural = "Сообщения"