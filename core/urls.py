from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # front-end index page
    url(r'^ag/public/index/$', views.index, name='publicIndex'),
    # front-end home page
    url(r'^$', views.home, name='publicHome'),
]
