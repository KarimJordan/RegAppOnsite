from django.contrib import admin
from .models import Layout, LayoutField, LayoutFieldValue

# Register your models here.
admin.site.register(Layout)
admin.site.register(LayoutField)
admin.site.register(LayoutFieldValue)
