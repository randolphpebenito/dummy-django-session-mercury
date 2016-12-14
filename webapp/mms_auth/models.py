from __future__ import unicode_literals
from random import randint

from django.conf import settings
from django.db import models


class MsisdnUrl(models.Model):
    msisdn = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
            )   
    short_code = models.CharField(max_length=12)
    timestamp  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.msisdn)


