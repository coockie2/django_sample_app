# -*- coding: utf-8 -*-
from django import forms

class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')
