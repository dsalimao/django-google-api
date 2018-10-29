from django.urls import re_path, path
from . import views

app_name = 'gmail'

urlpatterns = [
    re_path(r'^start_oauth_flow', views.start_oauth_flow, name='start_oauth_flow'),
    re_path(r'^oauth_return', views.oauth_return, name='oauth_return'),
    re_path(r'^index', views.index, name='index'),
    re_path(r'^messages', views.messages, name='messages'),
]