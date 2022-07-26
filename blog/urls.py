

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post,category, about




app_name = "blog"


urlpatterns = [
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('blog/<slug:url>', post, name="blog"),
    path('category/<slug:url>',category, name="category"),
]
