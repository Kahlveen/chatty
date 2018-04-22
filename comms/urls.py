from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('send_msg',views.send_msg,name='send_msg'),
]
