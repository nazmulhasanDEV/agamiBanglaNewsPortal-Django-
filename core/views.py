from django.shortcuts import render, redirect, get_object_or_404
import datetime
from adminPanel.models import SiteLogo, BreakingNews, CoverNewsMain, CoverNews1, CoverNews2, CoverNews3, CoverNews4, NewsCategories

def index(request):
    # grabing site logo from db
    site_logo_db = SiteLogo.objects.filter().first()

    context = {
        'breaking_news': breaking_news,
        'is_duration_ends': is_duration_has,

        # site logo
        'site_logo': site_logo_db,
    }

    return render(request, 'frontEnd/index.html', context)

def home(request):

    # grabing the breaking news from db
    breaking_news = BreakingNews.objects.filter().last()

    # getting the duration of breaking news will stay for
    is_duration_has = 0
    if breaking_news:
        news_duration_seted_up = breaking_news.duration.days

        # finding duration after adding the breaking news
        duration_till_now = (datetime.datetime.now().day) - (breaking_news.added_at.day)

        if duration_till_now == 0 or duration_till_now == 1:
            is_duration_has += 1

    # grabing site logo from db
    site_logo_db = SiteLogo.objects.filter().first()

    # grabing cover news
    cover_news_main_db = CoverNewsMain.objects.filter().first()
    cover_news_catid = int(cover_news_main_db.cover_news_category)

    # gabing categories
    news_cats_db = NewsCategories.objects.all()

    # grabing cover_news_one
    cover_news_1_db = CoverNews1.objects.filter().first()
    cover_news_1_catid = int(cover_news_1_db.cover_news_category)

    # grabing cover_news_two
    cover_news_2_db = CoverNews2.objects.filter().first()
    cover_news_2_catid = int(cover_news_2_db.cover_news_category)

    # grabing cover_news_three
    cover_news_3_db = CoverNews3.objects.filter().first()
    cover_news_3_catid = int(cover_news_3_db.cover_news_category)

    # grabing cover_news_three
    cover_news_4_db = CoverNews4.objects.filter().first()
    cover_news_4_catid = int(cover_news_4_db.cover_news_category)

    context = {
        # cover news part two
        'cover_news_4_db': cover_news_4_db,
        'cover_news_4_catid': cover_news_4_catid,

        # cover news part two
        'cover_news_3_db': cover_news_3_db,
        'cover_news_3_catid': cover_news_3_catid,

        # cover news part two
        'cover_news_2_db': cover_news_2_db,
        'cover_news_2_catid': cover_news_2_catid,

        # cover news part one
        'cover_news_1_db' : cover_news_1_db,
        'cover_news_1_catid' : cover_news_1_catid,

        # breaking news part
        'breaking_news' : breaking_news,
        'is_duration_ends' : is_duration_has,

        # site logo
        'site_logo' : site_logo_db,

        # cover news main
        'cover_news_main' : cover_news_main_db,
        'cover_news_catid' : cover_news_catid,
        'news_cats_db' : news_cats_db,
    }

    return render(request, 'frontEnd/home.html', context)

