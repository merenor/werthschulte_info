from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from blog.models import MarketingElement


class MarketingElementSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return MarketingElement.objects.all()


class FlatPageSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return FlatPage.objects.all()
