from django.contrib import admin
from .models import Raffler, RafflerSelectionWinner, RafflerWinner

# Register your models here.
admin.site.register(Raffler)
admin.site.register(RafflerSelectionWinner)
admin.site.register(RafflerWinner)
