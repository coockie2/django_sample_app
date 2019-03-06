# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Friend, Message
from .forms import FriendForm, MessageForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Pythonでディレクトリの上層にあるモジュールをimportするときの注意点
# http://d.hatena.ne.jp/chlere/20110618/1308369842

# ユーザ一覧
class HelloListView(LoginRequiredMixin, ListView):
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
class HelloCreateView(LoginRequiredMixin, CreateView):
    model = Friend
    form_class = FriendForm
    template_name = "hello/create.html"
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー登録画面"
        return context

# ユーザ詳細
class HelloDetailView(LoginRequiredMixin, DetailView):
    model = Friend
    form_class = FriendForm
    template_name = "hello/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー詳細画面"
        return context

# ユーザ編集
class HelloUpdateView(LoginRequiredMixin, UpdateView):
    model = Friend
    form_class = FriendForm
    template_name = 'hello/update.html'
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー編集画面"
        return context

# ユーザ削除
class HelloDeleteView(LoginRequiredMixin, DeleteView):
    model = Friend
    form_class = FriendForm
    template_name = 'hello/delete.html'
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー削除画面"
        return context

#　メッセージ一覧
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'hello/message.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "メッセージ一覧画面"
        return context

# メッセージ登録
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'hello/message.html'
    success_url = "/hello"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "メッセージ登録画面"
        return context

# メッセージ詳細
class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    form_class = MessageForm
    template_name = 'hello/message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "メッセージ詳細画面"
        return context

