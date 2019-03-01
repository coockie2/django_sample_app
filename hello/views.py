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
