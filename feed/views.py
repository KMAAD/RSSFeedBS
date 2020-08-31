from django.shortcuts import render,redirect
from .forms import NewFeedForm
from .models import Feed
# Create your views here.


# This is where the user's RSS Feed information is rendered
def feed_home_view(request):
    feeds = Feed.objects.filter(userId = request.user.id)
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