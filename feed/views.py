from django.shortcuts import render, redirect
from .forms import NewFeedForm
from .models import Feed
import feedparser


# Create your views here.


# This is where the user's RSS Feed information is rendered for the home page
def feed_home_view(request):
    feeds = Feed.objects.filter(userId=request.user.id)
    form = NewFeedForm(initial={"userId": request.user.id})
    if request.method == "POST":
        form = NewFeedForm(request.POST)
        if form.is_valid():
            form.userId = request.user.id
            Feed.objects.create(**form.cleaned_data)
            return redirect('/user/userhome/')
        else:
            print(form.errors)
    context = {
        "form": form,
        "feeds": feeds
    }
    return render(request, 'user/userhome.html', context)


# Renders the desired RSS Feed
def RSS_URL_View(request, id, orderby):
    feeds = Feed.objects.filter(userId=request.user.id)
    form = NewFeedForm(initial={"userId": request.user.id})
    if request.method == "POST":
        form = NewFeedForm(request.POST)
        if form.is_valid():
            form.userId = request.user.id
            Feed.objects.create(**form.cleaned_data)
            return redirect('/user/userhome/')
        else:
            print(form.errors)
    rss_url = Feed.objects.values("link").get(id=id)
    rss_url = rss_url["link"]
    parser = feedparser.parse(rss_url)
    context = {
        "user": request.user.id,
        "path": request.path,
        "feeds": feeds,
        "form": form,
        "url": rss_url,
        "parser": parser
    }
    return render(request, "rss/rss.html", context)
