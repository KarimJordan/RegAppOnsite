from django.contrib import admin
from .models import Guest, GuestInfo, GuestInfoField
# Register your models here.

admin.site.register(Guest)
admin.site.register(GuestInfo)
admin.site.register(GuestInfoField)