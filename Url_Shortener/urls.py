from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from shortener.views import open_short_url

import shortener

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('Profile.urls')),
    url(r'^', include('shortener.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)