from django.contrib.sitemaps import Sitemap

from .models import GadgetPost

class GadgetPostSitemap(Sitemap):
        changefreq = "weekly"
        priority = 0.9

        def items(self):
                return GadgetPost.objects.all()

        def location(self, obj):
                return "/reviews/" + str(obj)
