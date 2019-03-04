# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from sns.models.group import Group

# Friendモデル
class Friend(models.Model):
    # 外部キーの設定
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
                              related_name='friend_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + '(group:"' + str(self.group) + '")'

