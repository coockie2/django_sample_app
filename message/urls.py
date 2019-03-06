# -*- coding: utf-8 -*-

from django.urls import path
from message.views.message_list_view import MessageListView

app_name = 'message'
urlpatterns = [
    path('', MessageListView.as_view(), name = 'index'),
]
