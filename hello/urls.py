from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.HelloListView.as_view(), name = 'index'),
    path('create/', views.HelloCreateView, name = 'create'),
    path('update/<int:pk>/', views.HelloUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>', views.HelloDeleteView.as_view(), name = 'delete'),
#    path('check', views.check, name = 'check'),
#    path('message', views.message, name = 'message'),
#    path('message/<int:page>', views.message, name = 'message'),
]
