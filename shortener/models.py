from django.db import models
#from django.contrib import auth
from Url_Shortener import settings

class LongURL(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class ShortURL(models.Model):
    name = models.CharField(max_length = 50)
    number_of_clicks = models.IntegerField(default=0)
    link_to_long = models.ForeignKey(LongURL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=0, null = True)
    created_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name