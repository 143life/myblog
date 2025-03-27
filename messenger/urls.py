from django.urls import path
from . import views

urlpatterns = [
	path('', views.RoomView.as_view(), name='create-room'),
	path('<str:room_name>/<str:username>/', views.MessageView.as_view(), name='room')
]