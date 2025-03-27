from django.contrib import admin

from .models import *

# 5. Добавить модели в админку (чтобы администритор смог их редактировать)
admin.site.register(Room)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ('room', 'sender')