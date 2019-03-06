# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Messageモデル
class Message(models.Model):

    # 外部キーの設定
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # テーブルの項目を定義
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content) + '(' + str(self.owner) + ')'

    class Meta:
        ordering = ('-pub_date',)

