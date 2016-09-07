from django.db import models
from django.contrib.auth.models import User
from Url_Shortener import settings
from Profile.models import Profile
#from django.contrib import auth


class LongURL(models.Model):
    name = models.CharField(max_length = 100)
    ads  = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class ShortURL(models.Model):
    name = models.CharField(max_length = 50)
    clicks = models.IntegerField(default=0)
    long_link = models.ForeignKey(LongURL)
    user = models.ForeignKey(User, default=0, null = True)
    created_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name