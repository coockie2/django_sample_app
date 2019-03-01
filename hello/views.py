# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    print 'hello#index'
    params = {
            'title' : 'Hello/Index',
            'msg' : 'これは、サンプルで作ったページです。',
            'goto' : 'next',
        }
    return render(request, 'hello/index.html', params)

def next(request):
    print 'hello#next'
    params = {
            'title' : 'Hello/Next',
            'msg' : 'これは、もう1つのページです。',
            'goto' : 'index',
        }
    return render(request, 'hello/index.html', params)
