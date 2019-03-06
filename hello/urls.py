from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.HelloListView.as_view(), name = 'index'),
    path('detail/<int:pk>', views.HelloDetailView.as_view(), name = 'detail'),
    path('create/', views.HelloCreateView.as_view(), name = 'create'),
    path('update/<int:pk>', views.HelloUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>', views.HelloDeleteView.as_view(), name = 'delete'),
#    path('check', views.check, name = 'check'),
    path('message', views.MessageListView.as_view(), name = 'message'),
#    path('message/create', views.MessageCreateView.as_view(), name = 'message:create'),
#    path('message/detail/<int:pk>', views.MessageDetailView.as_view(), name = 'message:detail'),
]
