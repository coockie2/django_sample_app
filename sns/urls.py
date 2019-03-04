from django.urls import path
from .views import index, groups, add, creategroup, post, share, good

urlpatterns = [
    path('', index.index, name='index'),
    path('groups', groups.groups, name='groups'),
    path('add', add.add, name='add'),
    path('creategroup', creategroup.creategroup, name='creategroup'),
    path('post', post.post, name='post'),
    path('share/<int:share_id>', share.share, name='share'),
    path('good/<int:good_id>', good.good, name='good'),
]

