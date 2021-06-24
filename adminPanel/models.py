from django.db import models
from user.models import User

# user/admin/staff's profile images
class UserProfileImage(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    profileImg = models.ImageField()

    def __str__(self):
        return str(self.user)

# news categories
class NewsCategories(models.Model):
    category_name = models.CharField(default='', max_length=255, verbose_name="News Category Name")

    def __str__(self):
        return str(self.category_name)+ "|" + str(self.pk)

# news subcategories
class NewsSubCategories(models.Model):
    category         = models.ForeignKey(NewsCategories, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return str(self.category)+"|"+str(self.subcategory_name)

# breaking news model
class BreakingNews(models.Model):
    breaking_news = models.TextField(max_length=70, blank=True, null=True)
    added_at      = models.DateField(auto_now_add=True)
    duration      = models.DurationField()

    def __str__(self):
        return "Breaking News-" + str(self.pk)

# site logo
class SiteLogo(models.Model):
    site_logo = models.ImageField()
    def __str__(self):
        return "Site Setting-" + str(self.pk)

# site social media info
class SocialMediaLink(models.Model):
    site_fb_link = models.TextField(default="", blank=True, null=True)
    site_tw_link = models.TextField(default="", blank=True, null=True)
    site_instagram_link = models.TextField(default="", blank=True, null=True)
    site_youtube_link = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return "Social Media Links:" + str(self.pk)

# editor and publisher info
class EditorPublisher(models.Model):
    editor_name    = models.CharField(max_length=255, default="")
    publisher_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return "EP:" + str(self.pk)


# cover news part for home page
class CoverNewsMain(models.Model):
    cover_news_image       = models.ImageField()
    cover_news_title       = models.TextField(max_length=255, verbose_name="Cover News Title")
    cover_news_category    = models.CharField(max_length=255, default="")
    cover_news_subcategory = models.CharField(max_length=255, blank=True, null=True)
    cover_news_details     = models.TextField(max_length=2000, blank=True, null=True)
    cover_news_added_at    = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Main Cover News:-" + str(self.pk)

class CoverNews1(models.Model):
    cover_news_image = models.ImageField()
    cover_news_title = models.TextField(max_length=255, verbose_name="Cover News Title")
    cover_news_category = models.CharField(max_length=255, default="")
    cover_news_subcategory = models.CharField(max_length=255, blank=True, null=True)
    cover_news_details = models.TextField(max_length=2000, blank=True, null=True)
    cover_news_added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Cover News One:-" + str(self.pk)


class CoverNews2(models.Model):
    cover_news_image = models.ImageField()
    cover_news_title = models.TextField(max_length=255, verbose_name="Cover News Title")
    cover_news_category = models.CharField(max_length=255, default="")
    cover_news_subcategory = models.CharField(max_length=255, blank=True, null=True)
    cover_news_details = models.TextField(max_length=2000, blank=True, null=True)
    cover_news_added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Cover News Two:-" + str(self.pk)

class CoverNews3(models.Model):
    cover_news_image = models.ImageField()
    cover_news_title = models.TextField(max_length=255, verbose_name="Cover News Title")
    cover_news_category = models.CharField(max_length=255, default="")
    cover_news_subcategory = models.CharField(max_length=255, blank=True, null=True)
    cover_news_details = models.TextField(max_length=2000, blank=True, null=True)
    cover_news_added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Cover News Three:-" + str(self.pk)

class CoverNews4(models.Model):
    cover_news_image = models.ImageField()
    cover_news_title = models.TextField(max_length=255, verbose_name="Cover News Title")
    cover_news_category = models.CharField(max_length=255, default="")
    cover_news_subcategory = models.CharField(max_length=255, blank=True, null=True)
    cover_news_details = models.TextField(max_length=2000, blank=True, null=True)
    cover_news_added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Cover News Four:-" + str(self.pk)

# Most recent news
class MostRecent(models.Model):
    news_image       = models.ImageField()
    news_title       = models.TextField(max_length=255)
    news_description = models.TextField(max_length=1000)
    news_writer      = models.CharField(max_length=70, blank=True, null=True)
    news_visitors    = models.IntegerField(blank=True, null=True)
    news_details = models.TextField(max_length=2000, blank=True, null=True)
    news_added_at    = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Most Recent: "+ str(self.pk)


# Most popular news
class MostPopular(models.Model):
    news_image = models.ImageField()
    news_title = models.TextField(max_length=255)
    news_description = models.TextField(max_length=1000)
    news_writer = models.CharField(max_length=70, blank=True, null=True)
    news_visitors = models.IntegerField(blank=True, null=True)
    news_details = models.TextField(max_length=2000, blank=True, null=True)
    news_added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Most Popular: " + str(self.pk)

# main news model
class NewsMain(models.Model):
    news_image            = models.ImageField()
    news_title            = models.TextField(max_length=255)
    news_description      = models.TextField(max_length=1000)
    news_writer           = models.CharField(max_length=70, blank=True, null=True)
    news_visitors         = models.IntegerField(default=0, blank=True, null=True)
    news_comments         = models.IntegerField(default=0, blank=True, null=True)
    news_tags             = models.TextField(default="", blank=True, null=True)
    news_category_name    = models.CharField(max_length=255, blank=True, null=True)
    news_catid            = models.IntegerField(default=0)
    news_subcategory_name = models.CharField(max_length=255, blank=True, null=True)
    news_subcatid         = models.IntegerField(default=0)
    news_added_at         = models.DateField(auto_now_add=True)


    def __str__(self):
        return "Main News: " + str(self.pk)