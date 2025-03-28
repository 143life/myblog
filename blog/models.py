from django.db import models

class Post(models.Model):
	'''данные о записи в блоге'''
	title = models.CharField('Заголовок записи', max_length = 100)
	description = models.TextField('Текст записи')
	author = models.CharField('Имя автора', max_length = 50)
	date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return f'{self.title}, {self.author}'

	class Meta:
		verbose_name = 'Запись'
		verbose_name_plural = 'Записи'