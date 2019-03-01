# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import HelloForm

def index(request):
    params = {
            'title' : 'Hello',
            'data' : Friend.objects.all(),
        }
    return render(request, 'hello/index.html', params)

def create(request):
    params = {
            'title' : 'Hello',
            'form' : HelloForm(),
        }
    if (request.method == 'POST'):
        Friend(name     = request.POST['name'], \
               mail     = request.POST['mail'], \
               gender   = 'gender' in request.POST, \
               age      = request.POST['age'], \
               birthday = int(request.POST['birthday'])).save
        return redirect(to='hello/')
    return render(request, 'hello/create.html', params)
