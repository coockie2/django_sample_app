# -*- coding: utf-8 -*-

from django.urls import path
from . import views
 
app_name = 'graph'
urlpatterns = [
    path('', views.index, name='index'),
    path('charts/simple.png', views.simple, name='charts'),
]