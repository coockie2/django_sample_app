# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from ..models import Message, Group
from ..forms import PostForm

from django.contrib.auth.decorators import login_required

from . import common

# メッセージのポスト処理
@login_required(login_url='/admin/login/')
def post(request):
    # POST送信の処理
    if request.method == 'POST':
        # 送信内容の取得
        gr_name = request.POST['groups']
        content = request.POST['content']
        # Groupの取得
        group = Group.objects.filter(owner=request.user) \
                .filter(title=gr_name).first()
        if group == None:
            (pub_user, group) = common.Common.get_public()
        # Messageを作成し設定して保存
        msg = Message()
        msg.owner = request.user
        msg.group = group
        msg.content = content
        msg.save()
        # メッセージを設定
        messages.success(request, '新しいメッセージを投稿しました！')
        return redirect(to='/sns')
    
    # GETアクセス時の処理
    else:
        form = PostForm(request.user)
    
    # 共通処理
    params = {
            'login_user':request.user,
            'form':form,
        }
    return render(request, 'sns/post.html', params)
