from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django_summernote.admin import SummernoteModelAdmin

from .models import BlogEntry, MarketingElement

# MarketingElement
# Apply summernote to all TextField in model.
class MarketingElementAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(MarketingElement, MarketingElementAdmin)

# BlogEntry
class BlogEntryAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(BlogEntry, BlogEntryAdmin)

# Flatpages
class FlatPageAdmin(SummernoteModelAdmin):
    pass

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
