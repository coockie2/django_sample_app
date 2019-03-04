# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from sns.models.message import Message

# Goodモデル
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
                              related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for "' + str(self.message) + '" (by ' + \
                str(self.owner) + ')'
