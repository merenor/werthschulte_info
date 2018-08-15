"""werthschulte_info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flatpage_views
from blog import views as blog_views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import FlatPageSitemap, MarketingElementSitemap


sitemaps = {
    'flatpages': FlatPageSitemap,
    'marketingelements': MarketingElementSitemap,
}


urlpatterns = [

    # Editor / Admin
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Flatpages
    url(r'^kontakt/$', flatpage_views.flatpage, {'url': '/kontakt/'},
        name='kontakt'),
    url(r'^impressum/$', flatpage_views.flatpage, {'url': '/impressum/'},
        name='impressum'),
    url(r'^datenschutz/$', flatpage_views.flatpage, {'url': '/datenschutz/'},
        name='datenschutz'),
    url(r'^pgp-key/$', flatpage_views.flatpage, {'url': '/pgp-key/'},
        name='pgp-key'),

    # Neue-Medien-Blog
    url(r'^neuemedien/$', blog_views.neue_medien_blog_redirect,
        name='neue-medien-blog-redirect'),

    # Marketing-Elements
    url(r'^(?P<slug>[\w\-]+)/$', blog_views.marketing_detail,
        name='marketing_slug_detail'),


    # Sitemap for Google
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    # Index
    url(r'^$', blog_views.index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
