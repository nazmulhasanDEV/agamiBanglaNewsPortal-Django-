from django.shortcuts import render, redirect, get_object_or_404
import datetime
from adminPanel.models import SiteContactInfo, Visitor_message, NewsSubCategories, SiteLogo, BreakingNews, CoverNewsMain, CoverNews1, CoverNews2, CoverNews3, CoverNews4, NewsCategories, NewsMain, MostRecent, MostPopular, EditorPublisher
from django.contrib import messages

def index(request):
    # grabing site logo from db
    site_logo_db = SiteLogo.objects.filter().first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # find out category which has no sub-category
    category_list_which_has_no_subcat = []
    for x in news_category_model:
        is_exist_cat_in_subcat = subcategory_model.filter(category=x.pk).first()
        if is_exist_cat_in_subcat is None:
            category_list_which_has_no_subcat.append(x.pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    context = {

        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # list of category which has no sub-category
        'category_list_which_has_no_subcat' : category_list_which_has_no_subcat,

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
    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = 'Not Found!'

    # grabing cover news
    cover_news_main_db = CoverNewsMain.objects.filter().first()
    cover_news_catid = 0
    if cover_news_main_db:
        cover_news_catid += int(cover_news_main_db.cover_news_category)

    # gabing categories
    news_cats_db = NewsCategories.objects.all()

    # grabing cover_news_one
    cover_news_1_db = CoverNews1.objects.filter().first()
    cover_news_1_catid = 0
    if cover_news_1_db:
        cover_news_1_catid += int(cover_news_1_db.cover_news_category)

    # grabing cover_news_two
    cover_news_2_db = CoverNews2.objects.filter().first()
    cover_news_2_catid = 0
    if cover_news_2_db:
        cover_news_2_catid += int(cover_news_2_db.cover_news_category)

    # grabing cover_news_three
    cover_news_3_db = CoverNews3.objects.filter().first()
    cover_news_3_catid = 0
    if cover_news_3_db:
        cover_news_3_catid += int(cover_news_3_db.cover_news_category)

    # grabing cover_news_three
    cover_news_4_db = CoverNews4.objects.filter().first()
    cover_news_4_catid = 0
    if cover_news_4_db:
        cover_news_4_catid += int(cover_news_4_db.cover_news_category)

    # section started for those categories which has 1 or > 1 subcategories

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # find out category which has no sub-category
    category_list_which_has_no_subcat = []
    for x in news_category_model:
        is_exist_cat_in_subcat = subcategory_model.filter(category=x.pk).first()
        if is_exist_cat_in_subcat is None:
            category_list_which_has_no_subcat.append(x.pk)

    # news list of main news
    main_news_list = NewsMain.objects.all()

    # listing categories which has one or more subcategories
    news_cat_with_multiple_subcat = []

    # list of subcategories with single categories
    list_of_unique_subcategories = []
    list_of_unique_subcategories_pk = []

    # list of first subcategory pk of each single category
    list_of_first_subcat_of_single_category = []

    # list of last news added by it's subcategory for active tab. this is for active tab's big cover
    list_of_last_news_added_by_subcategory = []

    # list of news for active tab's small cover
    list_of_recent_news_for_small_cover = []

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # list of subcat pk's which has at least one main news
    list_of_subcat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_subcat_pk_which_has_atleast_one_news.append(news.news_subcatid)

    # storing all the pk of news category which has one or multiple sub-category
    for x in subcategory_model:
        if x.category.pk not in news_cat_with_multiple_subcat and x.category.pk != 9:
            news_cat_with_multiple_subcat.append(x.category.pk)

    # storing the first subcategory of a news category which has 1 or >1 sub-categoy
    for i in news_cat_with_multiple_subcat:
        first_subcat_id = NewsSubCategories.objects.filter(category=i).first()
        list_of_first_subcat_of_single_category.append(first_subcat_id.pk)

        # storing all the subcategories under a single news category
        list_of_unique_subcategories.append(NewsSubCategories.objects.filter(category=i))

    # storing the pk of all the unique sub-categories under a single news category
    for subcat_list in list_of_unique_subcategories:
        for subcat in subcat_list:
            list_of_unique_subcategories_pk.append(subcat.pk)

    # storing the last news and it's pk under a news sub-category
    for subcat_pk in list_of_unique_subcategories_pk:
        subcat_news_list_by_subcat = NewsMain.objects.filter(news_subcatid=subcat_pk)

        if subcat_news_list_by_subcat:
            last_news = subcat_news_list_by_subcat.last().pk
            list_of_last_news_added_by_subcategory.append(last_news)

            # storing most recent three news except the last added news
            list_of_recent_news_for_small_cover.append(
                subcat_news_list_by_subcat.exclude(pk=last_news).order_by("-pk")[:3])

    # section started for those categories which has 1 or > 1 subcategories

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"


    context = {

        # section for news category which has 1 or > 1 subcategory

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has no sub-category
        'category_list_which_has_no_subcat': category_list_which_has_no_subcat,

        # news list of main news
        'main_news_list': main_news_list,

        # list of last news added by subcategory for active tab's big cover
        'list_of_last_news_added_by_subcategory': list_of_last_news_added_by_subcategory,
        # list of most recent news for small cover of active tab
        'list_of_recent_news_for_small_cover': list_of_recent_news_for_small_cover,

        # list_of_first_subcat_of_single_category
        'list_of_first_subcat_of_single_category': list_of_first_subcat_of_single_category,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # list of subcat pk which has at least one main news
        'list_of_subcat_pk_which_has_atleast_one_news': list_of_subcat_pk_which_has_atleast_one_news,

        # news categories with one or multiple subcategories
        'news_cat_with_multiple_subcat': news_cat_with_multiple_subcat,

        # ends section for news category which has 1 or > 1 subcategory

        #editor publisher info
        'editor_publisher' : editor_publisher_info,

        # most recent news
        'most_recent_news' : most_recent_news,

        # most popular news
        'most_popular_news' : most_popular_news,

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

# getting subcategory list and news under them by their category
def news_list_by_category(request, catid):
    # grabing site logo from db
    site_logo_db = SiteLogo.objects.filter().first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # find out category which has no sub-category
    category_list_which_has_no_subcat = []
    for x in news_category_model:
        is_exist_cat_in_subcat = subcategory_model.filter(category=x.pk).first()
        if is_exist_cat_in_subcat is None:
            category_list_which_has_no_subcat.append(x.pk)

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # grabing all news from main news model

    news_list_by_pk = NewsMain.objects.filter(news_catid=catid).order_by("-pk")

    # storing all the subcatid from main news model
    list_of_subcatid_of_all_main_news = []
    for x in news_list_by_pk:
        if x.news_subcatid not in list_of_subcatid_of_all_main_news:
            list_of_subcatid_of_all_main_news.append(x.news_subcatid)


    # grabing subcategory by this category
    news_subcategory_of_this_category = NewsSubCategories.objects.filter(category=catid)

    # storing pk of subcategory of current category
    news_subcat_pk_list = []

    # storing only the news of the subcategory under this category
    main_news_list_by_subcat_pk = []

    for x in news_subcategory_of_this_category:
        news_subcat_pk_list.append(x.pk)

    for z in news_subcat_pk_list:
        main_news_list_by_subcat_pk.append(NewsMain.objects.filter(news_subcatid=z).order_by('-pk')[:3])

    last_news_of_category = None # storing the last news by category
    last_four_news_of_category = None # storing last four news by category

    # grabing the last news of the category
    pk_of_last_news_by_category = None
    if news_list_by_pk is not None and news_list_by_pk.count() > 0:
        pk_of_last_news_by_category = news_list_by_pk.first().pk # pk of the last news of the category
        if pk_of_last_news_by_category:
            last_news_of_category       = NewsMain.objects.filter(pk=pk_of_last_news_by_category).first() # last news of the category
            last_four_news_of_category  = news_list_by_pk.exclude(pk=pk_of_last_news_by_category)[:4] # last 4 news of the category except the last news


    context = {

        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has no sub-category
        'category_list_which_has_no_subcat': category_list_which_has_no_subcat,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # sending subcatid list which has at least one news in main news
        'list_of_subcatid_of_all_main_news' : list_of_subcatid_of_all_main_news,

        'main_news_list_by_subcat_pk' : main_news_list_by_subcat_pk,
        # sending news list by category from mailn news
        'news_list_by_pk': news_list_by_pk,

        # sending the pk of last news by single category
        'pk_of_last_news_by_category' : pk_of_last_news_by_category,
        # sending the last news
        'last_news_of_category' : last_news_of_category,
        # sending last four news of category
        'last_four_news_of_category' : last_four_news_of_category,
        # sending news-subcategories of category
        'news_subcategory_of_this_category' : news_subcategory_of_this_category,
    }

    return render(request, 'frontEnd/news_list_by_category.html', context)

def news_list_by_sub_category(request, subcat_id):

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # find out category which has no sub-category
    category_list_which_has_no_subcat = []
    for x in news_category_model:
        is_exist_cat_in_subcat = subcategory_model.filter(category=x.pk).first()
        if is_exist_cat_in_subcat is None:
            category_list_which_has_no_subcat.append(x.pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'

    # getting new by pk of their category
    main_news_list = NewsMain.objects.filter(news_subcatid=subcat_id).order_by("-pk")

    context = {

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,

        # site logo
        'site_logo': site_logo_db,

        # list of category which has no sub-category
        'category_list_which_has_no_subcat': category_list_which_has_no_subcat,

        'news_list_by_category' : main_news_list,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,
    }

    return render(request, 'frontEnd/news_list_by_sub_category.html', context)

# function for showing news list of single news category which has no news-subcategory
def news_list_by_category_has_not_subcat(request, cat_id):

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # find out category which has no sub-category
    category_list_which_has_no_subcat = []
    for x in news_category_model:
        is_exist_cat_in_subcat = subcategory_model.filter(category=x.pk).first()
        if is_exist_cat_in_subcat is None:
            category_list_which_has_no_subcat.append(x.pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'

    # getting new by pk of their category
    main_news_list = NewsMain.objects.filter(news_catid=cat_id).order_by("-pk")

    context = {

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,

        # site logo
        'site_logo': site_logo_db,

        # list of category which has no sub-category
        'category_list_which_has_no_subcat': category_list_which_has_no_subcat,

        'news_list_by_category' : main_news_list,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,
    }

    return render(request, 'frontEnd/news_list_of_single_category.html', context)


# cover news main details
def cover_news_main_details(request, pk):


    # grabing cover news one details
    cover_news_subcategory = CoverNewsMain.objects.filter(pk=pk).first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'


    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    context = {
        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,

        'cover_news_subcategory': cover_news_subcategory,

    }

    return render(request, "frontEnd/cover_news_main_details.html", context)


# cover news one details
def cover_news_1_details(request, pk):


    # grabing cover news one details
    cover_news_subcategory = CoverNews1.objects.filter(pk=pk).first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'


    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    context = {
        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,

        'cover_news_subcategory': cover_news_subcategory,

    }

    return render(request, "frontEnd/cover_news_1_details.html", context)

# cover news two details
def cover_news_2_details(request, pk):


    # grabing cover news one details
    cover_news_subcategory = CoverNews2.objects.filter(pk=pk).first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'


    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    context = {
        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,

        'cover_news_subcategory': cover_news_subcategory,

    }

    return render(request, "frontEnd/cover_news_2_details.html", context)

# cover news three details
def cover_news_3_details(request, pk):


    # grabing cover news one details
    cover_news_subcategory = CoverNews3.objects.filter(pk=pk).first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'


    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    context = {
        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,

        'cover_news_subcategory': cover_news_subcategory,

    }

    return render(request, "frontEnd/cover_news_3_details.html", context)

# cover news four details
def cover_news_4_details(request, pk):

    # grabing cover news one details
    cover_news_subcategory = CoverNews4.objects.filter(pk=pk).first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'


    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    context = {
        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,

        'cover_news_subcategory': cover_news_subcategory,

    }

    return render(request, "frontEnd/cover_news_4_details.html", context)

# main news details
def news_details(request, pk):

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"


    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    # grabing news by pk from db
    news_by_pk = NewsMain.objects.filter(pk=pk).first()


    context = {
        # news details
        'news_by_pk' : news_by_pk,

        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,

    }

    return render(request, "frontEnd/news_details.html", context)

# most popular news details
def most_popular_news_details(request, cat_id):

    # grabing news by pk from db
    news_by_pk = MostPopular.objects.filter(pk=cat_id).first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    # subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    context = {
        # news details
        'news_by_pk': news_by_pk,

        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,
    }

    return render(request, 'frontEnd/most_popular_news_details.html', context)


# most popular news details
def most_popular_news_details(request, cat_id):

    # grabing news by pk from db
    news_by_pk = MostPopular.objects.filter(pk=cat_id).first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    # subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    context = {
        # news details
        'news_by_pk': news_by_pk,

        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,
    }

    return render(request, 'frontEnd/most_popular_news_details.html', context)


# most popular news details
def most_recent_news_details(request, cat_id):

    # grabing news by pk from db
    news_by_pk = MostRecent.objects.filter(pk=cat_id).first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # grabing sucategory name and category name
    # subcategory_name = NewsCategories.objects.filter(pk=pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # most recent news
    if MostRecent.objects.count() > 0:
        most_recent_news = MostRecent.objects.all().order_by('-pk')[:5]
    else:
        most_recent_news = "Null"

    # most popular news
    if MostPopular.objects.count() > 0:
        most_popular_news = MostPopular.objects.all().order_by('-pk')[:5]
    else:
        most_popular_news = 'Null'

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    if SiteLogo.objects.count() > 0:
        site_logo_db = SiteLogo.objects.filter().first()
    else:
        site_logo_db = "Not found!"

    context = {
        # news details
        'news_by_pk': news_by_pk,

        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # most recent news
        'most_recent_news': most_recent_news,

        # most popular news
        'most_popular_news': most_popular_news,
    }

    return render(request, 'frontEnd/most_recent_news_details.html', context)

# contact us
def contact_us(request):
    # grabing site logo from db
    site_logo_db = SiteLogo.objects.filter().first()

    # grabing category model
    news_category_model = NewsCategories.objects.all()

    # grabing sub-cat model
    subcategory_model = NewsSubCategories.objects.all()

    # editor publisher info
    if EditorPublisher.objects.count() > 0:
        editor_publisher_info = EditorPublisher.objects.filter().first()
    else:
        editor_publisher_info = "Not added yet!"

    # find out category which has no sub-category
    category_list_which_has_no_subcat = []
    for x in news_category_model:
        is_exist_cat_in_subcat = subcategory_model.filter(category=x.pk).first()
        if is_exist_cat_in_subcat is None:
            category_list_which_has_no_subcat.append(x.pk)

    # list of category pk's which has at least one news under any subcategory
    list_of_cat_pk_which_has_atleast_one_news = []
    for news in NewsMain.objects.all():
        list_of_cat_pk_which_has_atleast_one_news.append(news.news_catid)

    # getting visitor's message
    if request.method == 'POST':
        visitor_name  = request.POST.get('name')
        visitor_email = request.POST.get('email')
        visitor_msg   = request.POST.get('msg')

        if visitor_name != '':
            visitor_msg_model = Visitor_message(visitor_name=visitor_name, visitor_email=visitor_email, visitor_text=visitor_msg)
            visitor_msg_model.save()
            messages.success(request, "Thanks for contacting with us! We will back to you soon!")
            return redirect('abContactUs')

    # grabing contact infos from db
    contact_info_db = SiteContactInfo.objects.filter().first()

    context = {

        # site logo
        'site_logo': site_logo_db,

        # news category model
        'news_category_model': news_category_model,

        # news subcategory model/list
        'subcategory_model': subcategory_model,

        # list of category which has at least one main news under it's any subcat
        'list_of_cat_pk_which_has_atleast_one_news': list_of_cat_pk_which_has_atleast_one_news,

        # list of category which has no sub-category
        'category_list_which_has_no_subcat': category_list_which_has_no_subcat,

        # editor publisher info
        'editor_publisher': editor_publisher_info,

        # site contact info
        'contact_info_db' : contact_info_db,

    }

    return render(request, 'frontEnd/contact.html', context)