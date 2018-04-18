import datetime

from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField(default=datetime.datetime.now(), null=False, blank=False)
    end_date = models.DateTimeField(default=datetime.datetime.now(), null=False, blank=False)
    venue = models.CharField(max_length=200, null=True)
    facebook_url = models.CharField(max_length=200, null=True)
    instagram_url = models.CharField(max_length=200, null=True)
    twitter_url = models.CharField(max_length=200, null=True)
    no_of_guest = models.IntegerField(null=False, blank=False)
