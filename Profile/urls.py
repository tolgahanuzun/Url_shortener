from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    url(r'^login/', 'Profile.views.login'),
    url(r'^logout/', 'Profile.views.logout'),
    url(r'^register/', 'Profile.views.register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
