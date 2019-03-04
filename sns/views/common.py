from django.contrib.auth.models import User

from ..models import Message, Friend, Group

from django.db.models import Q

class Common:
    # 指定されたグループおよび検索文字によるMessageの取得
    @staticmethod
    def get_your_group_message(owner, glist, find):
        # publicの取得
        (public_user, public_group) = Common.get_public()

        # チェックされたGroupの取得
        groups = Group.objects.filter(Q(owner=owner) \
                |Q(owner=public_user)).filter(title__in=glist)

        # Groupに含まれるFriendの取得
        me_friends = Friend.objects.filter(group__in=groups)

        # FriendのUserをリストにまとめる
        me_users = []
        for f in me_friends:
            me_users.append(f.user)

        # UserリストのUserが作ったGroupの取得
        his_groups = Group.objects.filter(owner__in=me_users)
        his_friends = Friend.objects.filter(user=owner) \
                .filter(group__in=his_groups)
        me_groups = []
        for hf in his_friends:
            me_groups.append(hf.group)

        # groupがgroupsに含まれるか、me_groupsに含まれるMessageの取得
        if find==None:
            messages = Message.objects.filter(Q(group__in=groups) \
                |Q(group__in=me_groups))[:100]
        else:
            messages = Message.objects.filter(Q(group__in=groups) \
                |Q(group__in=me_groups)) \
                .filter(content__contains=find)[:100]
        return messages
    
    # publicなUserとGroupを取得する
    @staticmethod
    def get_public():
        public_user = User.objects.filter(username='public').first()
        public_group = Group.objects.filter \
                (owner=public_user).first()
        return (public_user, public_group)
