from django.db import models

class News(models.Model):
	'''Данные о новости'''
	title = models.CharField('Заголовок', max_length=100)
	description = models.TextField('Текст новости')
	author = models.CharField('Автор', max_length=40)
	datetime = models.DateTimeField('Дата и время')

	def __str__(self):
		return f'{self.title}, {self.author}'
	
	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'