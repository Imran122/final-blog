from django.contrib.sitemaps import Sitemap

from .models import Post

class PostSitemap(Sitemap):
        changefreq = "weekly"
        priority = 0.9

        def items(self):
                return Post.objects.all()

        def location(self, obj):
                return "/blog/" + str(obj)
