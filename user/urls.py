from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^register/user/$', views.register_user, name='registerUser'),
    url(r'^login/user/$', views.login_user, name='loginUser'),
    url(r'^logout/user/$', views.login_user, name='logoutUser'),
]


