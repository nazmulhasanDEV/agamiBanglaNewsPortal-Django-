# Generated by Django 3.2.3 on 2021-06-21 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakingNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breaking_news', models.TextField(blank=True, max_length=70, null=True)),
                ('added_at', models.DateField(auto_now_add=True)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='CoverNews1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_news_image', models.ImageField(upload_to='')),
                ('cover_news_title', models.TextField(max_length=255, verbose_name='Cover News Title')),
                ('cover_news_category', models.CharField(default='', max_length=255)),
                ('cover_news_subcategory', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_news_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('cover_news_added_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoverNews2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_news_image', models.ImageField(upload_to='')),
                ('cover_news_title', models.TextField(max_length=255, verbose_name='Cover News Title')),
                ('cover_news_category', models.CharField(default='', max_length=255)),
                ('cover_news_subcategory', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_news_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('cover_news_added_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoverNews3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_news_image', models.ImageField(upload_to='')),
                ('cover_news_title', models.TextField(max_length=255, verbose_name='Cover News Title')),
                ('cover_news_category', models.CharField(default='', max_length=255)),
                ('cover_news_subcategory', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_news_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('cover_news_added_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoverNews4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_news_image', models.ImageField(upload_to='')),
                ('cover_news_title', models.TextField(max_length=255, verbose_name='Cover News Title')),
                ('cover_news_category', models.CharField(default='', max_length=255)),
                ('cover_news_subcategory', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_news_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('cover_news_added_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoverNewsMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_news_image', models.ImageField(upload_to='')),
                ('cover_news_title', models.TextField(max_length=255, verbose_name='Cover News Title')),
                ('cover_news_category', models.CharField(default='', max_length=255)),
                ('cover_news_subcategory', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_news_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('cover_news_added_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EditorPublisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor_name', models.CharField(default='', max_length=255)),
                ('publisher_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MostPopular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(upload_to='')),
                ('news_title', models.TextField(max_length=255)),
                ('news_description', models.TextField(max_length=1000)),
                ('news_writer', models.CharField(blank=True, max_length=70, null=True)),
                ('news_visitors', models.IntegerField(blank=True, null=True)),
                ('news_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('news_added_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MostRecent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(upload_to='')),
                ('news_title', models.TextField(max_length=255)),
                ('news_description', models.TextField(max_length=1000)),
                ('news_writer', models.CharField(blank=True, max_length=70, null=True)),
                ('news_visitors', models.IntegerField(blank=True, null=True)),
                ('news_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('news_added_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=255, verbose_name='News Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='NewsMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(upload_to='')),
                ('news_title', models.TextField(max_length=255)),
                ('news_description', models.TextField(max_length=1000)),
                ('news_writer', models.CharField(blank=True, max_length=70, null=True)),
                ('news_visitors', models.IntegerField(blank=True, default=0, null=True)),
                ('news_comments', models.IntegerField(blank=True, default=0, null=True)),
                ('news_tags', models.TextField(blank=True, default='', null=True)),
                ('news_category_name', models.CharField(blank=True, max_length=255, null=True)),
                ('news_catid', models.IntegerField(default=0)),
                ('news_subcategory_name', models.CharField(blank=True, max_length=255, null=True)),
                ('news_subcatid', models.IntegerField(default=0)),
                ('news_added_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_fb_link', models.TextField(blank=True, default='', null=True)),
                ('site_tw_link', models.TextField(blank=True, default='', null=True)),
                ('site_instagram_link', models.TextField(blank=True, default='', null=True)),
                ('site_youtube_link', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileImg', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsSubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(default='', max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminPanel.newscategories')),
            ],
        ),
    ]
