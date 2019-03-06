# -*- coding: utf-8 -*-

from django.views.generic import ListView

from message.models import Message

# Create your views here.
class MessageListView(ListView):
    model = Message
    template_name = 'message/index.html'
    paginate_by = 4
