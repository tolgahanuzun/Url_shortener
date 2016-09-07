from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return "%s" % (self.user)