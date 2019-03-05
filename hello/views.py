# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils import timezone

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Friend, Message
from .forms import FriendForm, FindForm, MessageForm

# Pythonでディレクトリの上層にあるモジュールをimportするときの注意点
# http://d.hatena.ne.jp/chlere/20110618/1308369842

# 一覧表示
class HelloListView(ListView):
    model = Friend
    template_name = 'hello/index.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー一覧画面"
        return context

#    def get_queryset(self):
#        object_list = self.model.objects.all().order_by('id')
#        q_friend= self.request.GET.get('friend')
#        if q_friend is not None:
#            if q_friend != "":
#                object_list = object_list.filter(friend=q_friend)
#        return object_list

# ユーザ登録
class HelloCreateView(CreateView):
    model = Friend
    form_class = FriendForm
    template_name = "hello/create.html"
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー登録画面"
        return context

# ユーザ編集
class HelloUpdateView(UpdateView):
    model = Friend
    form_class = FriendForm
    template_name = 'hello/update.html'
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー編集画面"
        return context

# ユーザ削除
class HelloDeleteView(DeleteView):
    model = Friend
    form_class = FriendForm
    template_name = 'hello/delete.html'
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー削除画面"
        return context

#def check(request):
#    params = {
#            'title' : 'Hello',
#            'message' : 'check validation.',
#            'form' : FriendForm(),
#        }
#    if (request.method == 'POST'):
#        obj = Friend()
#        form = FriendForm(request.POST, instance = obj)
#        params['form'] = form
#        if (form.is_valid()):
#            params['message'] = 'OK!'
#        else:
#            params['message'] = 'no good.'
#    return render (request, 'hello/check.html', params)

#def message(request, page = 1):
#    if (request.method == 'POST'):
#        MessageForm(request.POST, instance = Message()).save()
#    paginator = Paginator(Message.objects.all().reverse(), 5)
#    params = {
#            'title' : 'Message',
#            'form' : MessageForm(),
#            'data' : paginator.get_page(page),
#        }
#    return render(request, 'hello/message.html', params)
#
