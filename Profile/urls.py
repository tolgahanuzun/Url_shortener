from django.conf.urls import url

urlpatterns = [

    url(r'^login/', 'Profile.views.login'),
    url(r'^logout/', 'Profile.views.logout'),
    url(r'^register/', 'Profile.views.register'),
]
