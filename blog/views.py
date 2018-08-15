from django.shortcuts import render, redirect
from .models import BlogEntry, MarketingElement

# Create your views here.
def index(request):
    marketingelements = MarketingElement.objects.order_by("order")

    return render(request,
            'index.html',
            { 'marketingelements': marketingelements }
        )


def marketing_detail(request, slug):
    element = MarketingElement.objects.get(slug__iexact=slug)

    return render(request,
            'marketing_detail.html',
            { 'element': element }
        )


def neue_medien_blog_redirect(request):
    return redirect('http://neuemedien.werthschulte.info')
