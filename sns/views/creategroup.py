# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.contrib import messages

from ..models import Group

from django.contrib.auth.decorators import login_required

# グループの作成処理
@login_required(login_url='/admin/login/')
def creategroup(request):
    # Groupを作り、Userとtitleを設定して保存する
    gp = Group()
    gp.owner = request.user
    gp.title = request.POST['group_name']
    gp.save()
    messages.info(request, '新しいグループを作成しました。')
    return redirect(to='/sns/groups')
