from django.conf.urls import patterns,  include, url
from django.conf.urls.static import static
from shortener import views
from django.conf import settings

urlpatterns = [
    url(r'^add_url/', views.add_site),
    url(r'^([a-z]{5})/$', views.open_short_url),
    url(r'^$', views.add_site),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
