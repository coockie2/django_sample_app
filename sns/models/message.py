# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Messageモデル
class Message(models.Model):

    # 外部キーの設定
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
                              related_name='message_owner')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    # テーブルの項目を定義
    content = models.TextField(max_length=1000)
    share_id = models.IntegerField(default=-1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content) + '(' + str(self.owner) + ')'

    def get_share(self):
        return Message.objects.get(id=self.share_id)

    class Meta:
        ordering = ('-pub_date',)

