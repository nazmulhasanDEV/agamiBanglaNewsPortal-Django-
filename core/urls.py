from django.contrib import admin
from django.conf.urls import url, include
from . import views

# sitemap
# from django.contrib.sitemaps.views import sitemap
# from .sitemap import AgamiBanglaSiteMap
#
# newsSitemaps = {
#     'news' : AgamiBanglaSiteMap(),
# }


urlpatterns = [

    # sitemap
    # url(r'^sitemap\.xml$',sitemap, {'sitemaps': newsSitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # front-end index page
    url(r'^ag/public/index/$', views.index, name='publicIndex'),
    # front-end home page
    url(r'^$', views.home, name='publicHome'),

    # news list by category
    url(r'^ab/news/list/cat/(?P<catid>\d+)/$', views.news_list_by_category, name='abNewsListByCategoryPk'),
    url(r'^ab/news/list/(?P<subcat_id>\d+)/$', views.news_list_by_sub_category, name='abNewsListBySubCategory'),
    # url for function of news list which has no subcategory
    url(r'^ab/news/list/by/single/catgory/(?P<cat_id>\d+)/$', views.news_list_by_category_has_not_subcat, name="newsListByCatWhichHasNotSubcat"),

    # cover news details
    url(r'^ab/m_cover/news/details/(?P<pk>\d+)/$', views.cover_news_main_details, name='coverNewsMainDetails'),
    url(r'^ab/f_cover/news/details/(?P<pk>\d+)/$', views.cover_news_1_details, name='coverNews1Details'),
    url(r'^ab/t_cover/news/details/(?P<pk>\d+)/$', views.cover_news_2_details, name='coverNews2Details'),
    url(r'^ab/th_cover/news/details/(?P<pk>\d+)/$', views.cover_news_3_details, name='coverNews3Details'),
    url(r'^ab/fo_cover/news/details/(?P<pk>\d+)/$', views.cover_news_4_details, name='coverNews4Details'),

    # main news details
    url(r'^ab/news/details/(?P<pk>\d+)/$', views.news_details, name='abNewsDetails'),

    # most recent and popular news details
    url(r'^ab/news/most/popular/details/(?P<cat_id>\d+)/$', views.most_popular_news_details, name='newMostPopularDetails'),
    url(r'^ab/news/most/recent/details/(?P<cat_id>\d+)/$', views.most_recent_news_details, name='newMostRecentDetails'),

    # contact us
    url(r'^ab/news/contact/us/$', views.contact_us, name='abContactUs'),

    # about us
    url(r'^ab/about/us/$', views.about_us, name='abAbout'),


]
