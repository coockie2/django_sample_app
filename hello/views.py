# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Friend, Message
from .forms import FriendForm, FindForm, MessageForm

def index(request, num = 1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
            'title' : 'Hello',
            'message' : '',
            'data' : page.get_page(num),
        }
    return render(request, 'hello/index.html', params)

def create(request):
    if (request.method == 'POST'):
        FriendForm(request.POST, instance = Friend()).save()
        return redirect(to='hello/')
    params = {
            'title' : 'Hello',
            'form' : FriendForm(),
        }
    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id = num)
    if (request.method == 'POST'):
        FriendForm(request.POST, instance = obj).save()
        return redirect(to='/hello')
    params = {
            'title' : 'Hello',
            'id': num,
            'form' : FriendForm(instance = obj),
        }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id = num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
            'title' : 'Hello',
            'id': num,
            'obj' : friend,
        }
    return render(request, 'hello/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = Friend.objects.filter(name__contains = str)
    else:
        msg = 'search words ...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
            'title' : 'Hello',
            'message' : msg,
            'form' : form,
            'data' : data,
        }
    return render(request, 'hello/find.html', params)

def check(request):
    params = {
            'title' : 'Hello',
            'message' : 'check validation.',
            'form' : FriendForm(),
        }
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance = obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render (request, 'hello/check.html', params)

def message(request, page = 1):
    if (request.method == 'POST'):
        MessageForm(request.POST, instance = Message()).save()
    paginator = Paginator(Message.objects.all().reverse(), 5)
    params = {
            'title' : 'Message',
            'form' : MessageForm(),
            'data' : paginator.get_page(page),
        }
    return render(request, 'hello/message.html', params)