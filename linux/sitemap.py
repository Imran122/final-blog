from django.contrib.sitemaps import Sitemap

from .models import LinuxPost

class LinuxPostSitemap(Sitemap):
        changefreq = "weekly"
        priority = 0.9

        def items(self):
                return LinuxPost.objects.all()

        def location(self, obj):
                return "/linux/" + str(obj)
