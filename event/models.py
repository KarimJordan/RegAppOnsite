import datetime
from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(default=datetime.datetime.now(), null=False, blank=False)
    end_date = models.DateTimeField(default=datetime.datetime.now(), null=False, blank=False)
    venue = models.CharField(max_length=200, blank=True, null=True)
    facebook_url = models.CharField(max_length=200, blank=True, null=True)
    instagram_url = models.CharField(max_length=200, blank=True, null=True)
    twitter_url = models.CharField(max_length=200, blank=True, null=True)
    no_of_guest = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
