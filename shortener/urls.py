from django.conf.urls import patterns,  include, url
from shortener import views

urlpatterns = [
    url(r'^add_url/', views.add_site),
    url(r'^([a-z]{5})/$', views.open_short_url),
    url(r'^', views.add_site),
]
