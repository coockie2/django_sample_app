# -*- coding: utf-8 -*-

from django.urls import path
from upload_form import views

# app_name
# http://strkita.hatenablog.com/entry/2017/12/26/070954
app_name = 'upload_form'
urlpatterns = [
    path('', views.form, name = 'form'),
]