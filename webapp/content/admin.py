from django.contrib import admin
from .models import Msisdn

# Register your models here.
class MsisdnAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
admin.site.register(Msisdn, MsisdnAdmin)

