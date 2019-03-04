# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from ..models import Message, Group
from ..forms import PostForm

from django.contrib.auth.decorators import login_required

from . import common

# 投稿をシェアする
@login_required(login_url='/admin/login/')
def share(request, share_id):
    # シェアするMessageの取得
    share = Message.objects.get(id=share_id)
    
    # POST送信時の処理
    if request.method == 'POST':
        # 送信内容を取得
        gr_name = request.POST['groups']
        content = request.POST['content']
        # Groupの取得
        group = Group.objects.filter(owner=request.user) \
                .filter(title=gr_name).first()
        if group == None:
            (pub_user, group) = common.Common.get_public()

        # メッセージを作成し、設定をして保存
        msg = Message()
        msg.owner = request.user
        msg.group = group
        msg.content = content
        msg.share_id = share.id
        msg.save()

        share_msg = msg.get_share()
        share_msg.share_count += 1
        share_msg.save()

        # メッセージを設定
        messages.success(request, 'メッセージをシェアしました！')
        return redirect(to='/sns')
    
    # 共通処理
    form = PostForm(request.user)
    params = {
            'login_user':request.user,
            'form':form,
            'share':share,
        }
    return render(request, 'sns/share.html', params)
