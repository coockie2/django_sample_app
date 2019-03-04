# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Groupモデル
class Group(models.Model):

    # 外部キーの設定
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
                              related_name='group_owner')

    # テーブルの項目を定義
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
