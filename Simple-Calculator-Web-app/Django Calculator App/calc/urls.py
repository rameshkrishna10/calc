from django.conf.urls import url
from calc import views
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

