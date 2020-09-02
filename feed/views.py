from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewFeedForm
from .models import Feed
import feedparser


# Create your views here.


# This is where the user's RSS Feed information is rendered for the home page
@login_required(login_url='/home/')
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


# Renders the desired RSS Feed and ordering
@login_required(login_url='/home/')
def RSS_URL_View(request, id, orderby):
    feeds = Feed.objects.filter(userId=request.user.id)
    form = NewFeedForm(initial={"userId": request.user.id})
    error = ''
    if request.method == "POST":
        form = NewFeedForm(request.POST)
        if form.is_valid():
            form.userId = request.user.id
            Feed.objects.create(**form.cleaned_data)
            return redirect('/user/userhome/')
        else:
            print(form.errors)
    # Parses the RSS Feed
    rss_url = Feed.objects.values("link").get(id=id)
    rss_url = rss_url["link"]
    parser = feedparser.parse(rss_url)
    # Checks if feed is valid
    if parser.bozo == 1:
        error = 'There are no items in this feed. Please make sure the feed link is correct'
    # Sorting the RSS Feed
    try:
        if orderby == 'published_date':
            parser = sorted(parser.entries, key=lambda i: i['published'])
        elif orderby == 'title':
            parser = sorted(parser.entries, key=lambda i: i['title'])
        elif orderby == 'description':
            parser = sorted(parser.entries, key=lambda i: i['description'])
        elif orderby == 'none':
            parser = sorted(parser.entries, key=lambda i: i['title'])
        context = {
                "user": request.user.id,
                "path": request.path,
                "feeds": feeds,
                "form": form,
                "url": rss_url,
                "parser": parser,
                "linkid": id,
                "error": error
            }
    #In case of malformed RSS Fall back to sorting by title
    except KeyError:
        parser = sorted(parser.entries, key=lambda i: i['title'])
        context={
            "user": request.user.id,
            "path": request.path,
            "feeds": feeds,
            "form": form,
            "url": rss_url,
            "parser": parser,
            "linkid": id,
            "error": error
        }
    return render(request, "rss/rss.html", context)


# Delete an RSS Feed
@login_required(login_url='/home/')
def feed_delete_view(request, id):
    context = {
        "id": id
    }
    if request.method == "POST":
        Feed.objects.filter(id=id).delete()
        return redirect('/user/userhome/')
    else:
        return render(request,'rss/delete.html',context)
