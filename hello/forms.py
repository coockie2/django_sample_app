# -*- coding: utf-8 -*-
from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.CharField(label='age')
