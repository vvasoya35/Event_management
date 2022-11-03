from django.urls import path, include
from . import views

urlpatterns = [
    path('messageSend/', views.MessageSendPage,name='messageSendPage'),
    path('messageReceive/', views.MessageReceivePage,name='messageReceivePage'),
    path('create-message/<str:pk>', views.createMessage,name='create-message'),
]
