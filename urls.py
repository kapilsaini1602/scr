from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('login', views.homep, name="home"),
    url('logout', views.logout, name="logout"),
    url('welcome', views.homepwel, name="homewel"),
    url('reigster', views.regist, name="register"),
    url('forgot', views.forgot, name="forgot"),
    url('change_pass/<token>/', views.change_pass, name="change_pass"),

]
