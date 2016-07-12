from django.conf.urls import include, url
from django.contrib import admin
from shortener.views import open_short_url

import shortener

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('Profile.urls')),

    url(r'^', include('shortener.urls')),


]