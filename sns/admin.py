# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Friend, Message, Good, Group

# Register your models here.
admin.site.register(Friend)
admin.site.register(Good)
admin.site.register(Group)
admin.site.register(Message)
