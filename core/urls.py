from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # front-end index page
    url(r'^ag/public/index/$', views.index, name='publicIndex'),
    # front-end home page
    url(r'^$', views.home, name='publicHome'),

    # news list by category
    url(r'^ab/news/list/(?P<pk>\d+)/$', views.news_list_by_category, name='abNewsListByCategory'),

    # cover news details
    url(r'^ab/f_cover/news/details/(?P<pk>\d+)/$', views.cover_news_1_details, name='coverNews1Details'),
    url(r'^ab/t_cover/news/details/(?P<pk>\d+)/$', views.cover_news_2_details, name='coverNews2Details'),
    url(r'^ab/th_cover/news/details/(?P<pk>\d+)/$', views.cover_news_3_details, name='coverNews3Details'),
    url(r'^ab/fo_cover/news/details/(?P<pk>\d+)/$', views.cover_news_4_details, name='coverNews4Details'),

    # main news details
    url(r'^ab/news/details/(?P<pk>\d+)/$', views.news_details, name='abNewsDetails'),


]
