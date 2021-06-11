from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^ag/admin/panel/index/$', views.admnPanel_index, name='adminPanelIndex'),
    url(r'^ag/admin/panel/home/$', views.adminPanel_home, name='adminPanelHome'),

    # url for adding new staff
    url(r'^ag/admin/panel/add/new/staff/$', views.adminPanel_addStaff, name='adminPanelAddStaff'),

    # deactivate staff account
    url(r'^ag/admin/panel/deactivate/user/account/(?P<pk>\d+)/$', views.adminPanel_deactivateStaffAccount, name='adminPanelDeactivateStaffAccnt'),
    url(r'^ag/admin/panel/activate/user/account/(?P<pk>\d+)/$', views.adminPanel_activateStaffAccount, name='adminPanelActivateStaffAccnt'),
    url(r'^ag/admin/panel/remove/staff/user/(?P<pk>\d+)/$', views.adminPanel_removeStaffAccount, name='adminPanelRemoveStaffAccnt'),

    url(r'^ag/admin/panel/update/profile/pic/$', views.adminPanel_profilePic, name='adminPanelProfilePic'),
    url(r'^ag/admin/panel/change/password/$', views.adminPanel_changePassword, name='adminPanelChangePassword'),
    # news category adding url
    url(r'^ag/admin/panel/news/cats/$', views.adminPanel_newsCategory, name='adminPanelNewsCats'),

    # news subcategory adding url
    url(r'^ag/admin/panel/add/news/subcats/$', views.adminPanel_newsSubCategory, name='adminPanelAddNewsSubCats'),
    url(r'^ag/admin/panel/news/subcat/list/(?P<pk>\d+)/$', views.adminPanel_newsSubCatList, name='adminPanelNewsSubCatList'),

    #delete news subcategory from the list
    url(r'^ag/admin/panel/del/news/subcat/(?P<pk>\d+)/$', views.adminPanel_newsSubCatDelete, name='adminPanelDelNewsSubcat'),

    # breaking news section
    url(r'^ag/admin/panel/add/breaking-news/$', views.adminPanel_addBreakingNews, name='adminPanelAddBreakingNews'),
    url(r'^ag/admin/panel/delete/breaking-news/(?P<pk>\d+)/$', views.adminPanel_deleteBreakingNews, name="adminPanelDeleteBreakingNews"),

    # site setting
    url(r'^ag/admin/panel/site/setting/$', views.adminPanel_siteSetting, name='adminPanel_siteSetting'),
    url(r'^ag/admin/panel/update/site/logo/$', views.adminPanel_updateSiteLogo, name='adminPanelUpdateSiteLogo'),

    #social media link setup
    url(r'^ag/admin/panel/add/social/links/$', views.adminPanel_addSocialMediaLink, name='adminPanelAddSocialMediaLink'),
    url(r'^ag/admin/panel/edit/social/media/links/(?P<pk>\d+)/$', views.adminPanel_editSocialMediaLinks, name='adminPanelEditlSocialMediaLink'),
    url(r'^ag/admin/panel/delete/site/logo/(?P<pk>\d+)/$', views.adminPanel_delSiteLogo, name='adminPanelDelSiteLogo'),

    # editor and publisher set up
    url(r'^ag/admin/panel/add/editor/publisher/$', views.adminPanel_addEditorPublisher, name='adminPanelEditorPublisher'),
    url(r'^ag/admin/panel/edit/editor/publisher/(?P<pk>\d+)/$', views.adminPanel_editEditorPublisher, name='adminPanelEditEditorPublisher'),

    # cover news setting
    url(r'^ag/admin/add/cover/news/$', views.adminPanel_addCoverNews, name='adminPanelAddCoverNews'),

    # main cover news part
    url(r'^ag/admin/add/main/cover/news/$', views.adminPanel_addMainCoverNews, name='adminPanelAddMainCoverNews'),
    url(r'^aga/admin/edit/main/cover/news/(?P<pk>\d+)/$', views.adminPanel_editMainCoverNews, name='adminPanelEditMainCoverNews'),

    # cover news one
    url(r'^ag/admin/add/cover/news/one/$', views.adminPanel_addCoverNewsOne, name='adminPanelAddCoverNews1'),
    url(r'^aga/admin/edit/cover/news/one/(?P<pk>\d+)/$', views.adminPanel_editCoverNewsOne, name='adminPanelEditCoverNews1'),

    # cover news two
    url(r'^ag/admin/add/cover/news/two/$', views.adminPanel_addCoverNewsTwo, name='adminPanelAddCoverNews2'),
    url(r'^aga/admin/edit/cover/news/two/(?P<pk>\d+)/$', views.adminPanel_editCoverNewsTwo, name='adminPanelEditCoverNews2'),

    # cover news three
    url(r'^ag/admin/add/cover/news/three/$', views.adminPanel_addCoverNewsThree, name='adminPanelAddCoverNews3'),
    url(r'^aga/admin/edit/cover/news/three/(?P<pk>\d+)/$', views.adminPanel_editCoverNewsThree, name='adminPanelEditCoverNews3'),

    # cover news four
    url(r'^ag/admin/add/cover/news/four/$', views.adminPanel_addCoverNewsFour, name='adminPanelAddCoverNews4'),
    url(r'^aga/admin/edit/cover/news/four/(?P<pk>\d+)/$', views.adminPanel_editCoverNewsFour, name='adminPanelEditCoverNews4'),

    # cover news list
    url(r'^ag/admin/cover/news/list/$', views.adminPanel_coverNewsList, name='adminPanelCoverNewsList'),

    # most recent
    url(r'^ag/admin/add/most/recent/$', views.adminPanel_addMostRecentNews, name='adminPanelAddMostRecent'),
    url(r'^ag/admin/edit/most/recent/news/(?P<pk>\d+)/$', views.adminPanel_editMostRecentNews, name='adminPanelEditMostRecent'),
    url(r'^ag/admin/del/most/recent/news/(?P<pk>\d+)/$', views.adminPanel_delMostRecentNews, name='adminPanelDeleteMostRecent'),

    # most popular
    url(r'^ag/admin/add/most/popular/$', views.adminPanel_addMostPopularNews, name='adminPanelAddMostPopular'),
    url(r'^ag/admin/edit/most/popular/news/(?P<pk>\d+)/$', views.adminPanel_editMostPopularNews, name='adminPanelEditMostPopular'),
    url(r'^ag/admin/delete/most/popular/news/(?P<pk>\d+)/$', views.adminPanel_deleteMostPopularNews, name='adminPanelDeleteMostPopular'),

]



