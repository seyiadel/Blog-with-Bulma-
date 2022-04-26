from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Category, Post

class CategorySitemap(Sitemap):
    def item(self):
        return Category.objects.all

class PostSitemap(Sitemap):
    def item(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self,obj):
        return obj.created_at