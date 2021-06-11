from django.shortcuts import render, redirect, get_object_or_404
import datetime
from adminPanel.models import BreakingNews

def index(request):

    return render(request, 'frontEnd/index.html')

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

    context = {
        'breaking_news' : breaking_news,
        'is_duration_ends' : is_duration_has,
    }

    return render(request, 'frontEnd/home.html', context)

