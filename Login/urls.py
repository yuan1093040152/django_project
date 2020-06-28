from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login,name='login'),  #登录
    url(r'^successful/$', views.successful,name='successful'),   #注册成功
    url(r'^login/logout/$', views.logout,name='logout'),  #注销
    url(r'^login_successful/$', views.login_successful,name='login_successful'),    #登录成功
    url(r'^login/register/$', views.register,name='register'),    #注册请求
    url(r'^login/login_info/$', views.login_info,name='login_info'),   #登录请求
    url(r'^login/go_login/$', views.go_login,name='go_login'),   #去登录
]