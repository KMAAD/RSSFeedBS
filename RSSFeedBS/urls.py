"""RSSFeedBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from user.views import user_login_view, user_signup_view, user_signout
from feed.views import feed_home_view,RSS_URL_View, feed_delete_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login_view),
    path('home/', user_login_view),
    path('logout/', user_signout),
    path('user/signup/', user_signup_view),
    path('user/userhome/', feed_home_view),
    path('user/userhome/rss/<int:id>/<str:orderby>',RSS_URL_View),
    path('rss/<int:id>/delete', feed_delete_view)


]
