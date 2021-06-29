from django.contrib import admin
from .models import *

admin.site.register(UserProfileImage)
admin.site.register(NewsCategories)
admin.site.register(NewsSubCategories)
admin.site.register(BreakingNews)
admin.site.register(SiteLogo)
admin.site.register(SocialMediaLink)
admin.site.register(EditorPublisher)

# update site contact info
admin.site.register(SiteContactInfo)

# home page cover news part
admin.site.register(CoverNewsMain)
admin.site.register(CoverNews1)
admin.site.register(CoverNews2)
admin.site.register(CoverNews3)
admin.site.register(CoverNews4)

# most recent and popular
admin.site.register(MostRecent)
admin.site.register(MostPopular)

# main news model
admin.site.register(NewsMain)

# visitor's message
admin.site.register(Visitor_message)