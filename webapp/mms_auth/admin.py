from django.contrib import admin
from .models import MsisdnUrl

class MsisdnUrlAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
admin.site.register(MsisdnUrl, MsisdnUrlAdmin)
