from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
import bot.views
urlpatterns = [
    path('', views.index,name='index'),
    url(r'^post_message/', bot.views.post_message, name='post_message'),
]