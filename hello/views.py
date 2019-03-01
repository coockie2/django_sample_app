# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm

def index(request):
    params = {
            'title' : 'Hello',
            'data' : Friend.objects.all(),
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
