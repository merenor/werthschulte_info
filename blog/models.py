from django.db import models
from django.utils import timezone

# Create your models here.
class MarketingElement(models.Model):
    """
    My marketing element
    """

    class Meta:
        ordering = ['order']

    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=31, unique=True,
        help_text="A label for URL config.")
    headline = models.CharField(max_length=255, default='')
    pic = models.ImageField(upload_to='img/marketing/')
    shorttext = models.CharField(max_length=255, default='')
    longtext = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.headline


class BlogEntry(models.Model):
    """
    My special blog class
    """

    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = "Blog entries"

    headline = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=31, unique=True,
        help_text="A label for URL config.")
    teaserpic = models.ImageField(upload_to='img/blog/teaser/', null=True,
        blank=True)
    longtext = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.headline
