# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

from ..models import Friend

from django.contrib.auth.decorators import login_required

from . import common

# Friendの追加処理
@login_required(login_url='/admin/login/')
def add(request):
    # 追加するUserを取得
    add_name = request.GET['name']
    add_user = User.objects.filter(username=add_name).first()
    # Userが本人だった場合の処理
    if add_user == request.user:
        messages.info(request, "自分自身をFriendに追加することはできません。")
        return redirect(to='/sns')
    # publicの取得
    (public_user, public_group) = common.Common.get_public()
    # add_userのFriendの数を調べる
    frd_num = Friend.objects.filter(owner=request.user) \
            .filter(user=add_user).count()
    # ゼロより大きければ既に登録済み
    if frd_num > 0:
        messages.info(request, add_user.username + \
                ' は既に追加されています。')
        return redirect(to='/sns')
    
    # ここからFriendの登録処理
    frd = Friend()
    frd.owner = request.user
    frd.user = add_user
    frd.group = public_group
    frd.save()
    # メッセージを設定
    messages.success(request, add_user.username + ' を追加しました！　\
            groupページに移動して、追加したFriendをメンバーに設定して下さい。')
    return redirect(to='/sns')
