from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from user.models import User
from .models import *
from datetime import timedelta
import datetime
from django.http import JsonResponse


# @login_required(login_url='/login/user')
def admnPanel_index(request):

    if request.user.is_authenticated:
        username = request.user.user_name

    # profile picture
    profile_pic = UserProfileImage.objects.filter(user=request.user).first()

    context = {
        'username' : username,
        'profile_pic': profile_pic,
    }

    return render(request, 'backEnd/index.html', context)

# @login_required(login_url='/login/user')
def adminPanel_home(request):

    return render(request, 'backEnd/home.html')


# function for adding new staff
# @login_required(login_url='/login/user')
def adminPanel_addStaff(request):

    if request.method == 'POST':
        staff_fname            = request.POST.get('staff-first-name')
        staff_lname            = request.POST.get('staff-last-name')
        staff_email            = request.POST.get('staff-email')
        staff_username         = request.POST.get('staff-username')
        staff_password         = request.POST.get('password')
        staff_confirm_password = request.POST.get('confirm-pass')

        if staff_password == staff_confirm_password:
            if len(User.objects.filter(email=staff_email)) == 0 and len(User.objects.filter(user_name=staff_username))==0:
                user = User.objects.create_user(email=staff_email, user_name=staff_username, password=staff_password)
                user.first_name = staff_fname
                user.last_name  = staff_lname
                user.is_active  = True
                user.is_Staff   = True
                user.save()
                messages.success(request, "New staff account has been created successfully!")
                return redirect('adminPanelAddStaff')
            else:
                messages.warning(request, "Email or Username already exists!")
                return redirect('adminPanelAddStaff')
        else:
            messages.warning(request, "Password didn't match!")
            return redirect('adminPanelAddStaff')

    staff_user = User.objects.filter(is_Staff=True)

    context = {
        'staff_user' : staff_user,
    }

    return render(request, 'backEnd/staff-setting.html', context)


# deactivate staff account
# @login_required(login_url='/login/user')
def adminPanel_deactivateStaffAccount(request, pk):

    try:
        user = User.objects.filter(pk=pk).first()
        user.is_active = False
        user.save()
        messages.success(request, "Successfully deactivated this account!")
        return redirect("adminPanelAddStaff")
    except:
        messages.warning(request, "User not found!")
        return redirect("adminPanelAddStaff")
    return redirect("adminPanelAddStaff")


# activate staff account
# @login_required(login_url='/login/user')
def adminPanel_activateStaffAccount(request, pk):

    try:
        user = User.objects.filter(pk=pk).first()
        user.is_active = True
        user.save()
        messages.success(request, "Successfully activated this account!")
        return redirect("adminPanelAddStaff")
    except:
        messages.warning(request, "User not found!")
        return redirect("adminPanelAddStaff")
    return redirect("adminPanelAddStaff")



# remove staff account
# @login_required(login_url='/login/user')
def adminPanel_removeStaffAccount(request, pk):

    try:
        user = User.objects.filter(pk=pk).first()
        user.delete()
        messages.success(request, "Successfully deleted a staff account!")
        return redirect("adminPanelAddStaff")
    except:
        messages.warning(request, "User not found!")
        return redirect("adminPanelAddStaff")
    return redirect("adminPanelAddStaff")

# @login_required(login_url='/login/user')
def adminPanel_profilePic(request):
    # profile picture
    profile_pic = UserProfileImage.objects.filter(user=request.user).first()

    if request.method == 'POST':
        img = request.FILES['profile-pic']
        try:
            if len(UserProfileImage.objects.filter(user=request.user)) <= 0:
                user = UserProfileImage(user=request.user, profileImg=img)
                user.save()
                messages.success(request, "Profile picture has been added!")
                return redirect('adminPanelProfilePic')
            else:
                fs = FileSystemStorage()
                user = UserProfileImage.objects.filter(user=request.user).first()
                fs.delete(user.profileImg.name)
                user.profileImg = img
                user.save()
                messages.success(request, "Your profile picture has been updated!")
                return redirect('adminPanelProfilePic')
        except:
            messages.warning(request, "No image found!")
            return redirect('adminPanelProfilePic')


    context = {
        'profile_pic': profile_pic,
    }

    return render(request, 'backEnd/profile_setting.html', context)

# @login_required(login_url='/login/user')
def adminPanel_changePassword(request):

    if request.method == 'POST':
        email        = request.POST.get('pass-email')
        old_pass     = request.POST.get('old-pass')
        new_pass     = request.POST.get('new-pass')
        confirm_pass = request.POST.get('confirm-pass')

        if new_pass == confirm_pass:
            user = User.objects.filter(user_name=request.user.user_name).first()
            if email == request.user.email:
                authenticate_user = authenticate(request, email=email, password=old_pass)
                if authenticate_user is not None:
                    user.set_password(new_pass)
                    user.save()
                    return redirect('registerUser')
                else:
                    messages.warning(request, "User not found!")
                    return redirect('adminPanelChangePassword')
            else:
                messages.warning(request, "Entered wrong email! Try again!")
                return redirect('adminPanelChangePassword')
        else:
            messages.warning(request, "Password didn't match!")


    return render(request, 'backEnd/profile_setting.html')

# news categories
# @login_required(login_url='/login/user')
def adminPanel_newsCategory(request):

    if request.method == 'POST':
        category_name = request.POST.get('news-category')

        if category_name:
            news_cats = NewsCategories(category_name=category_name)
            news_cats.save()
            messages.success(request, "New category has been added!")
            return redirect('adminPanelNewsCats')
        else:
            messages.warning(request, "There is something wrong!")
            return redirect('adminPanelNewsCats')

    # grabing all the categories
    cat_list = NewsCategories.objects.all()

    context = {
        'category_list' : cat_list,
    }

    return render(request, 'backEnd/news_category.html', context)

# news categories
# @login_required(login_url='/login/user')
def adminPanel_newsCategory(request):

    if request.method == 'POST':
        category_name = request.POST.get('news-category')

        if category_name:
            news_cats = NewsCategories(category_name=category_name)
            news_cats.save()
            messages.success(request, "New category has been added!")
            return redirect('adminPanelNewsCats')
        else:
            messages.warning(request, "There is something wrong!")
            return redirect('adminPanelNewsCats')

    # grabing all the categories
    cat_list = NewsCategories.objects.all()

    context = {
        'category_list' : cat_list,
    }

    return render(request, 'backEnd/news_category.html', context)

# news categories & subcategories
# @login_required(login_url='/login/user')
def adminPanel_newsSubCategory(request):

    if request.method == 'POST':
        category_id = request.POST.get('select-news-category')
        subcat_name   = request.POST.get('news-subcategory')

        if category_id:
            news_cat     = NewsCategories.objects.filter(pk=category_id).first()
            news_subcats = NewsSubCategories(category=news_cat, subcategory_name=subcat_name)
            news_subcats.save()
            messages.success(request, "New subcategory has been added!")
            return redirect('adminPanelNewsCats')
        else:
            messages.warning(request, "There is something wrong!")
            return redirect('adminPanelNewsCats')

    # grabing all the categories
    cat_list = NewsCategories.objects.all()

    context = {
        'category_list': cat_list,
    }

    return render(request, 'backEnd/news_category.html', context)


# news subcategories list
# @login_required(login_url='/login/user')
def adminPanel_newsSubCatList(request, pk):

    # grabing all the news subcategories based on news category pk
    news_cat = NewsCategories.objects.filter(pk=pk).first()
    news_subcat_list = NewsSubCategories.objects.filter(category=news_cat)


    context = {
        'news_subcategories_list' : news_subcat_list,
    }

    return render(request, 'backEnd/news_subcat_list.html', context)

# delete news subcategories from the list
# @login_required(login_url='/login/user')
def adminPanel_newsSubCatDelete(request, pk):

    try:
        news_subcat = NewsSubCategories.objects.filter(pk=pk).first()
        news_subcat.delete()
        messages.success(request, "Deleted successfully!")
        return redirect('adminPanelNewsSubCatList', pk=pk)
    except:
        messages.warning(request, "Something went wrong! Try again!")
        return redirect('adminPanelNewsSubCatList', pk=pk)

    return redirect('adminPanelNewsSubCatList', pk=pk)

# breaking news section
# @login_required(login_url='/login/user')
def adminPanel_addBreakingNews(request):

    if request.method == 'POST':
        breaking_news          = request.POST.get('breaking-news')
        breaking_news_duration = request.POST.get('select-news-category')

        if len(breaking_news) <= 70:
            # max_duration = breaking_news_duration
            breaking_news_db = BreakingNews(breaking_news=breaking_news, duration=timedelta(days=int(breaking_news_duration)))
            breaking_news_db.save()
            messages.success(request, f"Breaking news added for {breaking_news_duration} days!")
            return redirect('adminPanelAddBreakingNews')
        else:
            messages.success(request, "Use maximum 70 characters!")
            return redirect('adminPanelAddBreakingNews')

    # accessing all data from db
    breaking_news_list = BreakingNews.objects.all().order_by("pk")

    context = {
        'breaking_news_list' : breaking_news_list,
    }

    return render(request, 'backEnd/add-breaking-news.html', context)

# delete breaking news
# @login_required(login_url='/login/user')
def adminPanel_deleteBreakingNews(request, pk):

    try:
        breaking_news = BreakingNews.objects.filter(pk=pk).first()
        breaking_news.delete()
        messages.success(request, "News has been deleted!")
        return redirect('adminPanelAddBreakingNews')

    except:
        messages.warning(request, "News not found to delete!")
        return redirect('adminPanelAddBreakingNews')

    return redirect('adminPanelAddBreakingNews')

# site setting function
# @login_required(login_url='/login/user')
def adminPanel_siteSetting(request):
    # grab existing editor publisher info
    editor_publisher_info = EditorPublisher.objects.filter().first()

    # grab social media links
    social_media_links = SocialMediaLink.objects.filter().first()

    # grab existing site logo
    logo_list = SiteLogo.objects.filter().first()

    context = {
        'site_logo': logo_list,
        'social_media_lnks': social_media_links,
        'editor_bpublisher_info': editor_publisher_info,
    }
    return render(request, 'backEnd/site-setting.html', context)

# Update site logo
# @login_required(login_url='/login/user')
def adminPanel_updateSiteLogo(request):

    if request.method == 'POST':
        site_logo = request.FILES['profile-pic']
        logo_extension = str(site_logo).split('.')
        valid_extension_list = ['png', 'jpeg', 'jpg']

        if logo_extension[1] in valid_extension_list:
            if len(SiteLogo.objects.all()) <= 0:
                logo_db = SiteLogo(site_logo=site_logo)
                logo_db.save()
                messages.success(request, "Updated your site logo!")
                return redirect('adminPanelUpdateSiteLogo')
            else:
                all_added_logo = SiteLogo.objects.all()
                for x in all_added_logo:
                    x.delete()
                logo_db = SiteLogo(site_logo=site_logo)
                logo_db.save()
                messages.success(request, "Update your site logo!")
        else:
            messages.warning(request, "File must in jpeg, jpg or png format!")
            return redirect('adminPanelUpdateSiteLogo')

    # grab existing site logo
    logo_list = SiteLogo.objects.filter().first()

    context = {
        'site_logo' : logo_list,
    }

    return render(request, "backEnd/site-setting.html", context)



# delete site logo
# @login_required(login_url='/login/user')
def adminPanel_delSiteLogo(request, pk):

    try:
        site_logo = SiteLogo.objects.filter(pk=pk).first()
        fs = FileSystemStorage()
        fs.delete(site_logo.site_logo.name)
        site_logo.delete()
        messages.success(request, "Deleted your logo! Please add new logo!")
        return redirect('adminPanelUpdateSiteLogo')
    except:
        messages.warning(request, "Logo not found!")
        return redirect('adminPanelUpdateSiteLogo')

    return redirect('adminPanelUpdateSiteLogo')

# add social media link here
# @login_required(login_url='/login/user')
def adminPanel_addSocialMediaLink(request):

    if request.method == 'POST':
        fb_link      = request.POST.get('fb_link')
        tw_link      = request.POST.get('tw_link')
        insta_link   = request.POST.get('youtube_link')
        youtube_link = request.POST.get('instagram_link')

        if fb_link != '' or tw_link != '' or insta_link != '' or youtube_link != '':
            if len(SocialMediaLink.objects.all()) <= 0:
                social_media_link_db = SocialMediaLink(site_fb_link=fb_link, site_tw_link=tw_link, site_instagram_link=insta_link,site_youtube_link=youtube_link)
                social_media_link_db.save()
                messages.success(request, "Social media link added!")
                return redirect('adminPanelAddSocialMediaLink')
            else:
                social_media_db = SocialMediaLink.objects.all()
                for x in social_media_db:
                    x.delete()
                save_social_media_lnk_db = SocialMediaLink(site_fb_link=fb_link, site_tw_link=tw_link, site_instagram_link=insta_link,site_youtube_link=youtube_link)
                save_social_media_lnk_db.save()
                messages.success(request, "Added social media links!")
                return redirect('adminPanelAddSocialMediaLink')

    # grab social media links
    social_media_links = SocialMediaLink.objects.filter().first()

    context = {
        'social_media_lnks' : social_media_links,
    }

    return render(request, "backEnd/site-setting.html", context)

# edit social media link here
# @login_required(login_url='/login/user')
def adminPanel_editSocialMediaLinks(request, pk):

    social_media_link_list = SocialMediaLink.objects.filter(pk=pk).first()

    if request.method == 'POST':
        fb_link = request.POST.get('fb_link')
        tw_link = request.POST.get('tw_link')
        insta_link = request.POST.get('youtube_link')
        youtube_link = request.POST.get('instagram_link')

        if fb_link != '' or tw_link != '' or insta_link != '' or youtube_link != '':
            sockial_media_link_db = SocialMediaLink.objects.filter(pk=pk).first()
            sockial_media_link_db.site_fb_link = fb_link
            sockial_media_link_db.site_tw_link = tw_link
            sockial_media_link_db.site_instagram_link = insta_link
            sockial_media_link_db.site_youtube_link   = youtube_link
            sockial_media_link_db.save()
            messages.success(request, "Successfully updated social media links!")
            return redirect('adminPanelAddSocialMediaLink')

    context = {
        'pk' : pk,
        'edit_social_media_Link' : social_media_link_list,
    }

    return render(request, 'backEnd/edit-social-media-link.html', context)


# add editor/publisher
# @login_required(login_url='/login/user')
def adminPanel_addEditorPublisher(request):

    if request.method == 'POST':
        editor_name = request.POST.get('editor-name')
        publisher_name = request.POST.get('publisher-name')

        if len(EditorPublisher.objects.all()) <= 0:
            editor_publisher_db = EditorPublisher(editor_name=editor_name, publisher_name=publisher_name)
            editor_publisher_db.save()
            messages.success(request, "Editor and Publisher has been added!")
            return redirect('adminPanel_siteSetting')
        else:
            editor_publisher_db = EditorPublisher.objects.all()
            for x in editor_publisher_db:
                x.delete()
            editor_publisher_save_newly_db = EditorPublisher(editor_name=editor_name, publisher_name=publisher_name)
            editor_publisher_save_newly_db.save()
            messages.success(request, "Editor and Publisher has been added!")
            return redirect('adminPanel_siteSetting')

    # grab existing editor publisher info
    editor_publisher_info = EditorPublisher.objects.filter().first()

    context = {
        'editor_bpublisher_info' : editor_publisher_info,
    }

    return render(request, 'backEnd/site-setting.html', context)


# edit editor/publisher
# @login_required(login_url='/login/user')
def adminPanel_editEditorPublisher(request, pk):

    existing_editor_publisher_info = EditorPublisher.objects.filter(pk=pk).first()

    if request.method == 'POST':
        editor_name    = request.POST.get('editor_name')
        publisher_name = request.POST.get('publisher_name')

        if editor_name != '' and publisher_name != '':
            editor_publisher_db = EditorPublisher.objects.filter(pk=pk).first()
            editor_publisher_db.editor_name    = editor_name
            editor_publisher_db.publisher_name = publisher_name
            editor_publisher_db.save()
            messages.success(request, "Updated editor and publisher info!")
            return redirect('adminPanel_siteSetting')
        else:
            messages.success(request, "Not found!")
            return redirect('adminPanel_siteSetting')

    context = {
        'pk' : pk,
        'existing_editor_publisher_info' : existing_editor_publisher_info,
    }
    return render(request, 'backEnd/edit-editor-publisher.html', context)


# cover news setting
# @login_required(login_url='/login/user')
def adminPanel_addCoverNews(request):


    # grabing all the news categories
    news_categories_list = NewsCategories.objects.all()

    # grabing main cover news info
    main_cover_news_info = CoverNewsMain.objects.filter().first()

    context = {
        'news_categories_list' : news_categories_list,
        'main_cover_news_info' : main_cover_news_info,
    }

    return render(request, "backEnd/add-cover-news.html", context)

# add main cover news
# @login_required(login_url='/login/user')
def adminPanel_addMainCoverNews(request):

    if request.method == "POST":
        img = request.FILES['main-cover-news-img']
        news_title = request.POST.get('cover_news_title')
        news_category = request.POST.get('select-cover-news-category')

        valid_file_extension = ['png', 'jpeg', 'jpg']
        img_extension = str(img).split('.')

        if img_extension[1] in valid_file_extension:
            if len(CoverNewsMain.objects.all()) <= 0:
                main_cover_news_db = CoverNewsMain(cover_news_image=img, cover_news_title=news_title, cover_news_category=news_category, cover_news_subcategory="Not Selected")
                main_cover_news_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')
            else:
                fs = FileSystemStorage()
                main_cover_news_db = CoverNewsMain.objects.all()
                for x in main_cover_news_db:
                    fs.delete(x.cover_news_image.name)
                    x.delete()
                save_main_cover_news_to_db = CoverNewsMain(cover_news_image=img, cover_news_title=news_title,cover_news_category=news_category, cover_news_subcategory="Not Selected")
                save_main_cover_news_to_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')

        else:
            messages.warning(request, "Only images are allowed!")
            return redirect('adminPanelAddCoverNews')

    context = {

    }

    return render(request, "backEnd/add-cover-news.html", context)


# Edit main cover news
# @login_required(login_url='/login/user')
def adminPanel_editMainCoverNews(request, pk):

    # grabing existing info
    main_cover_news_info = CoverNewsMain.objects.filter(pk=pk).first()
    cover_news_cat_id = int(main_cover_news_info.cover_news_category)

    # grabing news categories
    news_categories = NewsCategories.objects.all()

    if request.method == "POST":
        news_title = request.POST.get('edit_cover_news_title')
        news_category = request.POST.get('edit-select-cover-news-category')

        try:
            fs = FileSystemStorage()
            img = request.FILES['edi-main-cover-news-img']
            valid_file_extension = ['png', 'jpeg', 'jpg']
            img_extension = str(img).split('.')

            if img_extension[1] in valid_file_extension:
                update_db = CoverNewsMain.objects.filter(pk=pk).first()

                # deleting previous image
                fs.delete(update_db.cover_news_image.name)

                update_db.cover_news_image = img
                update_db.cover_news_title = news_title
                update_db.cover_news_category = news_category
                update_db.save()
                messages.success(request, "Update main cover news!")
                return redirect('adminPanelAddCoverNews')
            else:
                messages.success(request, "Only images(.jpeg, .jpg, .png) are allowed!")
                return redirect('adminPanelEditMainCoverNews',pk=pk)
        except:
            update_db = CoverNewsMain.objects.filter(pk=pk).first()
            update_db.cover_news_title = news_title
            update_db.cover_news_category = news_category
            update_db.save()
            messages.success(request, "Update main cover news!")
            return redirect('adminPanelAddCoverNews')

    context = {
        'pk' : pk,
        'main_cover_news_info' : main_cover_news_info,
        'main_cover_news_cat_id' : cover_news_cat_id,
        'news_categories' : news_categories,
    }

    return render(request, "backEnd/edit_main_cover_news.html", context)


# add cover news one
# @login_required(login_url='/login/user')
def adminPanel_addCoverNewsOne(request):

    if request.method == "POST":
        img = request.FILES['cover_news_one']
        news_title = request.POST.get('cover_news_one_title')
        news_category = request.POST.get('select-cover-news-category')

        valid_file_extension = ['png', 'jpeg', 'jpg']
        img_extension = str(img).split('.')

        if img_extension[1] in valid_file_extension:
            if len(CoverNews1.objects.all()) <= 0:
                cover_news_one_db = CoverNews1(cover_news_image=img, cover_news_title=news_title, cover_news_category=news_category, cover_news_subcategory="Not Selected")
                cover_news_one_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')
            else:
                fs = FileSystemStorage()
                cover_news_one_db = CoverNews1.objects.all()
                for x in cover_news_one_db:
                    fs.delete(x.cover_news_image.name)
                    x.delete()
                save_cover_news_one_to_db = CoverNews1(cover_news_image=img, cover_news_title=news_title,cover_news_category=news_category, cover_news_subcategory="Not Selected")
                save_cover_news_one_to_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')

        else:
            messages.warning(request, "Only images are allowed!")
            return redirect('adminPanelAddCoverNews')

    context = {

    }

    return render(request, "backEnd/add-cover-news.html", context)


# Edit cover news one
# @login_required(login_url='/login/user')
def adminPanel_editCoverNewsOne(request, pk):

    # grabing existing info
    cover_news_info_1 = CoverNews1.objects.filter(pk=pk).first()
    cover_news_cat_id = int(cover_news_info_1.cover_news_category)

    # grabing news categories
    news_categories = NewsCategories.objects.all()

    if request.method == "POST":
        news_title = request.POST.get('edit_cover_news_title')
        news_category = request.POST.get('edit-select-cover-news-category')

        try:
            fs = FileSystemStorage()
            img = request.FILES['edit-cover-news-one-img']
            valid_file_extension = ['png', 'jpeg', 'jpg']
            img_extension = str(img).split('.')

            if img_extension[1] in valid_file_extension:
                update_db = CoverNews1.objects.filter(pk=pk).first()

                # deleting previous image
                fs.delete(update_db.cover_news_image.name)

                update_db.cover_news_image = img
                update_db.cover_news_title = news_title
                update_db.cover_news_category = news_category
                update_db.save()
                messages.success(request, "Update main cover news!")
                return redirect('adminPanelCoverNewsList')
            else:
                messages.success(request, "Only images(.jpeg, .jpg, .png) are allowed!")
                return redirect('adminPanelEditCoverNews1',pk=pk)
        except:
            update_db = CoverNews1.objects.filter(pk=pk).first()
            update_db.cover_news_title = news_title
            update_db.cover_news_category = news_category
            update_db.save()
            messages.success(request, "Update main cover news!")
            return redirect('adminPanelCoverNewsList')

    context = {
        'pk' : pk,
        'cover_news_one_info' : cover_news_info_1,
        'cover_news_one_cat_id' : cover_news_cat_id,
        'news_categories' : news_categories,
    }

    return render(request, "backEnd/edit_cover_news_1.html", context)

# add cover news two
# @login_required(login_url='/login/user')
def adminPanel_addCoverNewsTwo(request):

    if request.method == "POST":
        img = request.FILES['cover_news_two']
        news_title = request.POST.get('cover_news_two_title')
        news_category = request.POST.get('select_cover_news_two_category')

        valid_file_extension = ['png', 'jpeg', 'jpg']
        img_extension = str(img).split('.')

        if img_extension[1] in valid_file_extension:
            if len(CoverNews2.objects.all()) <= 0:
                cover_news_two_db = CoverNews2(cover_news_image=img, cover_news_title=news_title, cover_news_category=news_category, cover_news_subcategory="Not Selected")
                cover_news_two_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')
            else:
                fs = FileSystemStorage()
                cover_news_two_db = CoverNews2.objects.all()
                for x in cover_news_two_db:
                    fs.delete(x.cover_news_image.name)
                    x.delete()
                save_cover_news_two_to_db = CoverNews2(cover_news_image=img, cover_news_title=news_title,cover_news_category=news_category, cover_news_subcategory="Not Selected")
                save_cover_news_two_to_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')

        else:
            messages.warning(request, "Only images are allowed!")
            return redirect('adminPanelAddCoverNews')

    context = {

    }

    return render(request, "backEnd/add-cover-news.html", context)


# Edit cover news two
# @login_required(login_url='/login/user')
def adminPanel_editCoverNewsTwo(request, pk):

    # grabing existing info
    cover_news_info_2 = CoverNews2.objects.filter(pk=pk).first()
    cover_news_cat_id = int(cover_news_info_2.cover_news_category)

    # grabing news categories
    news_categories = NewsCategories.objects.all()

    if request.method == "POST":
        news_title = request.POST.get('edit_cover_news_title')
        news_category = request.POST.get('edit-select-cover-news-category')

        try:
            fs = FileSystemStorage()
            img = request.FILES['edit-cover-news-one-img']
            valid_file_extension = ['png', 'jpeg', 'jpg']
            img_extension = str(img).split('.')

            if img_extension[1] in valid_file_extension:
                update_db = CoverNews2.objects.filter(pk=pk).first()

                # deleting previous image
                fs.delete(update_db.cover_news_image.name)

                update_db.cover_news_image = img
                update_db.cover_news_title = news_title
                update_db.cover_news_category = news_category
                update_db.save()
                messages.success(request, "Update main cover news!")
                return redirect('adminPanelCoverNewsList')
            else:
                messages.warning(request, "Only images(.jpeg, .jpg, .png) are allowed!")
                return redirect('adminPanelEditCoverNews2',pk=pk)
        except:
            update_db = CoverNews2.objects.filter(pk=pk).first()
            update_db.cover_news_title = news_title
            update_db.cover_news_category = news_category
            update_db.save()
            messages.success(request, "Update main cover news!")
            return redirect('adminPanelCoverNewsList')

    context = {
        'pk' : pk,
        'cover_news_two_info' : cover_news_info_2,
        'cover_news_two_cat_id' : cover_news_cat_id,
        'news_categories' : news_categories,
    }

    return render(request, "backEnd/edit_cover_news_2.html", context)


# add cover news three
# @login_required(login_url='/login/user')
def adminPanel_addCoverNewsThree(request):

    if request.method == "POST":
        img = request.FILES['cover_news_three']
        news_title = request.POST.get('cover_news_three_title')
        news_category = request.POST.get('select_cover_news_three_category')

        valid_file_extension = ['png', 'jpeg', 'jpg']
        img_extension = str(img).split('.')

        if img_extension[1] in valid_file_extension:
            if len(CoverNews3.objects.all()) <= 0:
                cover_news_three_db = CoverNews3(cover_news_image=img, cover_news_title=news_title, cover_news_category=news_category, cover_news_subcategory="Not Selected")
                cover_news_three_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')
            else:
                fs = FileSystemStorage()
                cover_news_three_db = CoverNews3.objects.all()
                for x in cover_news_three_db:
                    fs.delete(x.cover_news_image.name)
                    x.delete()
                save_cover_news_three_to_db = CoverNews3(cover_news_image=img, cover_news_title=news_title,cover_news_category=news_category, cover_news_subcategory="Not Selected")
                save_cover_news_three_to_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')

        else:
            messages.warning(request, "Only images are allowed!")
            return redirect('adminPanelAddCoverNews')

    context = {

    }

    return render(request, "backEnd/add-cover-news.html", context)


# Edit cover news three
# @login_required(login_url='/login/user')
def adminPanel_editCoverNewsThree(request, pk):

    # grabing existing info
    cover_news_info_3 = CoverNews3.objects.filter(pk=pk).first()
    cover_news_cat_id = int(cover_news_info_3.cover_news_category)

    # grabing news categories
    news_categories = NewsCategories.objects.all()

    if request.method == "POST":
        news_title = request.POST.get('edit_cover_news_title')
        news_category = request.POST.get('edit-select-cover-news-category')

        try:
            fs = FileSystemStorage()
            img = request.FILES['edit-cover-news-three-img']
            valid_file_extension = ['png', 'jpeg', 'jpg']
            img_extension = str(img).split('.')

            if img_extension[1] in valid_file_extension:
                update_db = CoverNews3.objects.filter(pk=pk).first()

                # deleting previous image
                fs.delete(update_db.cover_news_image.name)

                update_db.cover_news_image = img
                update_db.cover_news_title = news_title
                update_db.cover_news_category = news_category
                update_db.save()
                messages.success(request, "Updated cover news three!")
                return redirect('adminPanelCoverNewsList')
            else:
                messages.warning(request, "Only images(.jpeg, .jpg, .png) are allowed!")
                return redirect('adminPanelEditCoverNews3',pk=pk)
        except:
            update_db = CoverNews3.objects.filter(pk=pk).first()
            update_db.cover_news_title = news_title
            update_db.cover_news_category = news_category
            update_db.save()
            messages.success(request, "Update cover news three!")
            return redirect('adminPanelCoverNewsList')

    context = {
        'pk' : pk,
        'cover_news_three_info' : cover_news_info_3,
        'cover_news_three_cat_id' : cover_news_cat_id,
        'news_categories' : news_categories,
    }

    return render(request, "backEnd/edit_cover_news_3.html", context)


# add cover news four
# @login_required(login_url='/login/user')
def adminPanel_addCoverNewsFour(request):

    if request.method == "POST":
        img = request.FILES['cover_news_three']
        news_title = request.POST.get('cover_news_three_title')
        news_category = request.POST.get('select_cover_news_three_category')

        valid_file_extension = ['png', 'jpeg', 'jpg']
        img_extension = str(img).split('.')

        if img_extension[1] in valid_file_extension:
            if len(CoverNews4.objects.all()) <= 0:
                cover_news_four_db = CoverNews4(cover_news_image=img, cover_news_title=news_title, cover_news_category=news_category, cover_news_subcategory="Not Selected")
                cover_news_four_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')
            else:
                fs = FileSystemStorage()
                cover_news_four_db = CoverNews4.objects.all()
                for x in cover_news_four_db:
                    fs.delete(x.cover_news_image.name)
                    x.delete()
                save_cover_news_four_to_db = CoverNews4(cover_news_image=img, cover_news_title=news_title,cover_news_category=news_category, cover_news_subcategory="Not Selected")
                save_cover_news_four_to_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddCoverNews')

        else:
            messages.warning(request, "Only images(.jpeg, .jpg, .png) are allowed!")
            return redirect('adminPanelAddCoverNews')

    context = {

    }

    return render(request, "backEnd/add-cover-news.html", context)


# Edit cover news four
# @login_required(login_url='/login/user')
def adminPanel_editCoverNewsFour(request, pk):

    # grabing existing info
    cover_news_info_4 = CoverNews4.objects.filter(pk=pk).first()
    cover_news_cat_id = int(cover_news_info_4.cover_news_category)

    # grabing news categories
    news_categories = NewsCategories.objects.all()

    if request.method == "POST":
        news_title = request.POST.get('edit_cover_news_title')
        news_category = request.POST.get('edit-select-cover-news-category')

        try:
            fs = FileSystemStorage()
            img = request.FILES['edit-cover-news-four-img']
            valid_file_extension = ['png', 'jpeg', 'jpg']
            img_extension = str(img).split('.')

            if img_extension[1] in valid_file_extension:
                update_db = CoverNews4.objects.filter(pk=pk).first()

                # deleting previous image
                fs.delete(update_db.cover_news_image.name)

                update_db.cover_news_image = img
                update_db.cover_news_title = news_title
                update_db.cover_news_category = news_category
                update_db.save()
                messages.success(request, "Updated cover news three!")
                return redirect('adminPanelCoverNewsList')
            else:
                messages.warning(request, "Only images(.jpeg, .jpg, .png) are allowed!")
                return redirect('adminPanelEditCoverNews4',pk=pk)
        except:
            update_db = CoverNews4.objects.filter(pk=pk).first()
            update_db.cover_news_title = news_title
            update_db.cover_news_category = news_category
            update_db.save()
            messages.success(request, "Update cover news three!")
            return redirect('adminPanelCoverNewsList')

    context = {
        'pk' : pk,
        'cover_news_four_info' : cover_news_info_4,
        'cover_news_four_cat_id' : cover_news_cat_id,
        'news_categories' : news_categories,
    }

    return render(request, "backEnd/edit_cover_news_4.html", context)

# cover news list
# @login_required(login_url='/login/user')
def adminPanel_coverNewsList(request):

    # grab cover new one info
    cover_news_one_info = CoverNews1.objects.filter().first()

    # grab cover new one info
    cover_news_two_info = CoverNews2.objects.filter().first()

    # grab cover new one info
    cover_news_three_info = CoverNews3.objects.filter().first()

    # grab cover new one info
    cover_news_four_info = CoverNews4.objects.filter().first()

    context = {
        'cover_news_one_infor' : cover_news_one_info,
        'cover_news_two_infor' : cover_news_two_info,
        'cover_news_three_infor' : cover_news_three_info,
        'cover_news_four_infor' : cover_news_four_info,
    }
    return render(request, 'backEnd/cover_news_list.html', context)


# most recent news
# @login_required(login_url='/login/user')
def adminPanel_addMostRecentNews(request):

    # grabing all the most recent news from db
    most_recent_news_list = MostRecent.objects.all().order_by("-pk")[:2]

    if request.method == 'POST':
        news_img         = request.FILES['most_recent_img']
        news_title       = request.POST.get('most_recent_news_title')
        news_description = request.POST.get('most_recent_news_description')
        news_writer      = request.POST.get('news_writer')

        news_file_extension = str(news_img).split('.')
        valid_extension     = ['jpeg', 'jpg', 'png']

        if news_file_extension[1] in valid_extension:
            most_recent_news_db = MostRecent(news_image=news_img, news_title=news_title, news_description=news_description, news_writer=news_writer, news_visitors=0)
            most_recent_news_db.save()
            messages.success(request, "Save successfully!")
            return redirect('adminPanelAddMostRecent')
        else:
            messages.warning(request, "Only images (.jpeg, .jpg, .png) are allowed!")
            return redirect('adminPanelAddMostRecent')

    context = {
        'most_recent_news_list' : most_recent_news_list,
    }

    return render(request, 'backEnd/add_most_recent.html', context)

# most recent news
# @login_required(login_url='/login/user')
def adminPanel_editMostRecentNews(request, pk):

    # grabing existing data from db by pk
    existing_news_data = MostRecent.objects.filter(pk=pk).first()

    if request.method == 'POST':
        news_title = request.POST.get('most_recent_news_title')
        news_description = request.POST.get('most_recent_news_description')
        news_writer = request.POST.get('news_writer')

        try:
            fs = FileSystemStorage()
            img = request.FILES['most_recent_img']

            news_file_extension = str(img).split('.')
            valid_extension = ['jpeg', 'jpg', 'png']

            if news_file_extension[1] in valid_extension:
                #grab db by pk
                news_db = MostRecent.objects.filter(pk=pk).first()

                # deleting previous image
                fs.delete(news_db.news_image.name)

                # updating db with new data
                news_db.news_image = img
                news_db.news_title = news_title
                news_db.news_description = news_description
                news_db.news_writer = news_writer
                news_db.save()
                messages.success(request, "News updated!")
                return redirect('adminPanelAddMostRecent')
            else:
                messages.success(request, "Only images(.jpeg, .jpg, .png) are allowed!")
                return redirect('adminPanelEditMostRecent', pk=pk)
        except:
            # grab db by pk
            news_db = MostRecent.objects.filter(pk=pk).first()
            news_db.news_title = news_title
            news_db.news_description = news_description
            news_db.news_writer = news_writer
            news_db.save()
            messages.success(request, "News updated!")
            return redirect('adminPanelAddMostRecent')

    context = {
        'pk'  : pk,
        'existing_news_data' : existing_news_data,
    }
    return render(request, 'backEnd/edit_most_recent_news.html', context)

# most recent news
# @login_required(login_url='/login/user')
def adminPanel_delMostRecentNews(request, pk):

    try:
        fs = FileSystemStorage()
        news = MostRecent.objects.filter(pk=pk).first()
        fs.delete(news.news_image.name)
        news.delete()
        messages.success(request, "News has been deleted!")
        return redirect('adminPanelAddMostRecent')
    except:
        messages.success(request, "News not found!")
        return redirect('adminPanelAddMostRecent')

    return redirect('adminPanelAddMostRecent')


# most popular
# add most popular news
# @login_required(login_url='/login/user')
def adminPanel_addMostPopularNews(request):

    # grabing all the most recent news from db
    most_popular_news_list = MostPopular.objects.all().order_by("-pk")[:5]

    if request.method == 'POST':
        news_img         = request.FILES['most_popular_img']
        news_title       = request.POST.get('most_popular_news_title')
        news_description = request.POST.get('most_popular_news_description')
        news_writer      = request.POST.get('news_writer')

        news_file_extension = str(news_img).split('.')
        valid_extension     = ['jpeg', 'jpg', 'png']

        if news_file_extension[1] in valid_extension:
            most_recent_news_db = MostPopular(news_image=news_img, news_title=news_title, news_description=news_description, news_writer=news_writer, news_visitors=0)
            most_recent_news_db.save()
            messages.success(request, "Save successfully!")
            return redirect('adminPanelAddMostPopular')
        else:
            messages.warning(request, "Only images (.jpeg, .jpg, .png) are allowed!")
            return redirect('adminPanelAddMostPopular')

    context = {
        'most_popular_news_list' : most_popular_news_list,
    }

    return render(request, 'backEnd/add_most_popular.html', context)


# edit most popular news
# @login_required(login_url='/login/user')
def adminPanel_editMostPopularNews(request, pk):

    # grabing all the most recent news from db
    most_popular_news_list = MostPopular.objects.filter(pk=pk).first()

    if request.method == 'POST':
        news_title       = request.POST.get('most_popular_news_title')
        news_description = request.POST.get('most_popular_news_description')
        news_writer      = request.POST.get('news_writer')

        try:
            news_img = request.FILES['most_popular_img']
            news_file_extension = str(news_img).split('.')
            valid_extension = ['jpeg', 'jpg', 'png']

            if news_file_extension[1] in valid_extension:
                fs = FileSystemStorage()

                # grabing db by pk
                most_popular_news_db = MostPopular.objects.filter(pk=pk).first()

                # deleting previous image
                fs.delete(most_popular_news_db.news_image.name)

                # updating db with new data
                most_popular_news_db.news_image       = news_img
                most_popular_news_db.news_title       = news_title
                most_popular_news_db.news_description = news_description
                most_popular_news_db.news_writer      = news_writer
                most_popular_news_db.news_visitors    = 0
                most_popular_news_db.save()
                messages.success(request, "Saved successfully!")
                return redirect('adminPanelAddMostPopular')
            else:
                messages.warning(request, "Only images (.jpeg, .jpg, .png) are allowed!")
                return redirect('adminPanelEditMostPopular', pk=pk)

        except:
            # grabing db by pk
            most_popular_news_db = MostPopular.objects.filter(pk=pk).first()

            # updating db with new data
            most_popular_news_db.news_title = news_title
            most_popular_news_db.news_description = news_description
            most_popular_news_db.news_writer = news_writer
            most_popular_news_db.news_visitors = 0
            most_popular_news_db.save()
            messages.success(request, "Saved successfully!")
            return redirect('adminPanelAddMostPopular')

    context = {
        'pk' : pk,
        'most_popular_news_list' : most_popular_news_list,
    }

    return render(request, 'backEnd/edit_most_popular.html', context)


# edit most popular news
# @login_required(login_url='/login/user')
def adminPanel_deleteMostPopularNews(request, pk):

    try:
        fs = FileSystemStorage()
        news_db = MostPopular.objects.filter(pk=pk).first()
        fs.delete(news_db.news_image.name)
        news_db.delete()
        messages.success(request, "Deleted successfully!")
        return redirect('adminPanelAddMostPopular')
    except:
        messages.success(request, "News not found!")
        return redirect('adminPanelAddMostPopular')

    return redirect('adminPanelAddMostPopular')


# main news section starts

# add main news
# @login_required(login_url='/login/user')
def adminPanel_addMainNews(request):

    # grabing all the categories from db
    news_categories = NewsCategories.objects.all()

    # get selected category and it's pk from ajax request
    selected_cat_id = request.GET.get('news_cat_id')

    # grab all the sub-cats under selected cats
    subcat_list = list(NewsSubCategories.objects.filter(category=selected_cat_id).values())

    if request.is_ajax():
        return JsonResponse({'cat_id': selected_cat_id, 'sub_cat_list': subcat_list})

    # submitting data to db from news form
    if request.method == 'POST':
        news_file        = request.FILES['main_news_img']
        news_cat_id      = request.POST.get('select-main-news-category')
        news_sub_cat_id  = request.POST.get('select-main-news-subcategory')
        news_title       = request.POST.get('main_news_news_title')
        news_description = request.POST.get('main_news_description')
        news_writer      = request.POST.get('news_writer')

        file_extension = str(news_file).split('.')
        valid_extension = ['jpeg', 'jpg', 'png']

        if file_extension[1] in valid_extension:

            # grabing news subcat model
            news_subcat_db = NewsSubCategories.objects.filter(pk=news_sub_cat_id).first()
            # finding the name of news category
            news_cat_name = news_subcat_db.category.category_name
            # finding the name of news subcategory name
            news_subcat_name = news_subcat_db.subcategory_name

            main_news_db = NewsMain(
                news_image= news_file,
                news_title= news_title,
                news_description= news_description,
                news_writer= news_writer,
                news_visitors= 0,
                news_comments= 0,
                news_tags= "null",
                news_category_name= news_cat_name,
                news_catid= news_cat_id,
                news_subcategory_name= news_subcat_name,
                news_subcatid= news_sub_cat_id
            )
            main_news_db.save()
            messages.success(request, "News has been added!")
            return redirect('adminPanelAddMainNews')
        else:
            messages.warning(request, "Only images (.jpeg, jpg, png) are allowed!")
            return redirect('adminPanelAddMainNews')

    context = {
        'news_categories' : news_categories,
    }

    return render(request, "backEnd/add_main_news.html", context)

# main news list
# @login_required(login_url='/login/user')
def adminPanel_MainNewsList(request):

    # grabing all the main news
    main_news_list = NewsMain.objects.all()

    context = {
        'main_news_list' : main_news_list,
    }

    return render(request, "backEnd/main_news_list.html", context)


# main news list
# @login_required(login_url='/login/user')
def adminPanel_editMainNews(request, pk):

    # grabing news from db
    main_news_db = NewsMain.objects.filter(pk=pk).first()

    # grabing all the news categories
    news_cats = NewsCategories.objects.all()

    # grabing all the news categories
    news_subcats = NewsSubCategories.objects.all()

    # get selected category and it's pk from ajax request
    selected_cat_id = request.GET.get('news_cat_id')

    # grab all the sub-cats under selected cats
    subcat_list = list(NewsSubCategories.objects.filter(category=selected_cat_id).values())

    if request.is_ajax():
        return JsonResponse({'cat_id': selected_cat_id, 'sub_cat_list': subcat_list})

    # submitting data to db from news form
    if request.method == 'POST':

        news_cat_id = request.POST.get('select-main-news-category')
        news_sub_cat_id = request.POST.get('select-main-news-subcategory')
        news_title = request.POST.get('main_news_news_title')
        news_description = request.POST.get('main_news_description')
        news_writer = request.POST.get('news_writer')

        try:
            news_file = request.FILES['main_news_img']
            file_extension = str(news_file).split('.')
            valid_extension = ['jpeg', 'jpg', 'png']

            if file_extension[1] in valid_extension:

                fs = FileSystemStorage()

                # grabing news subcat model
                news_subcat_db = NewsSubCategories.objects.filter(pk=news_sub_cat_id).first()
                # finding the name of news category
                news_cat_name = news_subcat_db.category.category_name
                # finding the name of news subcategory name
                news_subcat_name = news_subcat_db.subcategory_name

                # grabing news db by pk
                main_news_db = NewsMain.objects.filter(pk=pk).first()
                # delete old image
                fs.delete(main_news_db.news_image.name)

                main_news_db.news_image= news_file
                main_news_db.news_title= news_title
                main_news_db.news_description= news_description
                main_news_db.news_writer= news_writer
                main_news_db.news_visitors= 0
                main_news_db.news_comments= 0
                main_news_db.news_tags= "null"
                main_news_db.news_category_name= news_cat_name
                main_news_db.news_catid= news_cat_id
                main_news_db.news_subcategory_name= news_subcat_name
                main_news_db.news_subcatid= news_sub_cat_id
                main_news_db.save()
                messages.success(request, "News has been added!")
                return redirect('adminPanelMainNewsList')
            else:
                messages.warning(request, "Only images (.jpeg, jpg, png) are allowed!")
                return redirect('adminPanelEditMainNews', pk=pk)
        except:
            # grabing news subcat model
            news_subcat_db = NewsSubCategories.objects.filter(pk=news_sub_cat_id).first()
            # finding the name of news category
            news_cat_name = news_subcat_db.category.category_name
            # finding the name of news subcategory name
            news_subcat_name = news_subcat_db.subcategory_name

            # grabing news db by pk
            main_news_db = NewsMain.objects.filter(pk=pk).first()
            main_news_db.news_title = news_title
            main_news_db.news_description = news_description
            main_news_db.news_writer = news_writer
            main_news_db.news_visitors = 0
            main_news_db.news_comments = 0
            main_news_db.news_tags = "null"
            main_news_db.news_category_name = news_cat_name
            main_news_db.news_catid = news_cat_id
            main_news_db.news_subcategory_name = news_subcat_name
            main_news_db.news_subcatid = news_sub_cat_id
            main_news_db.save()
            messages.success(request, "News has been updated!")
            return redirect('adminPanelMainNewsList')

    context = {
        'pk' : pk,
        'main_news_db' : main_news_db,
        'news_cats' : news_cats,
        'news_subcats' : news_subcats,
    }

    return render(request, "backEnd/edit_main_news.html", context)

# main news list
# @login_required(login_url='/login/user')
def adminPanel_deleteMainNews(request, pk):

    try:
        fs = FileSystemStorage()
        main_news_db = NewsMain.objects.filter(pk=pk).first()
        fs.delete(main_news_db.news_image.name)
        main_news_db.delete()
        messages.success(request, "News has been deleted!")
        return redirect('adminPanelMainNewsList')
    except:
        messages.warning(request, "News not found!")
        return redirect('adminPanelMainNewsList')

    return redirect('adminPanelMainNewsList')
