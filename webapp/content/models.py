from __future__ import unicode_literals
from random import randint

from django.db import models

# Create your models here.
class Msisdn(models.Model):
    msisdn  = models.CharField(max_length=12, blank=False)
    verif_code = models.CharField(max_length=12, null=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    date_modified  = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Msisdn"

    def __unicode__(self):
        return self.msisdn

    def set_verif_code(self, length):
        range_start = 10**(length-1)
        range_end = (10**length)-1
        self.verif_code = randint(range_start, range_end)
        return self.verif_code


#class Content(models.Model):


'''
Sample URL: [domain]/<content_type>/<short_code> (content_type, short_code)

Account (extend django user)
- msisdn

Account verif
- Account.uuid
- verif_code
- is_verified


Content
- content_type (eg: mp3, ftm)
- content_name (eg: puso_mo.<service_name>.mp3, pangako.<service_name>.ftm)
- created
- updated

ContentURL
- account
- short_code
- counter (required=False)
- content_id
- created
- updated


#Autodownload
def url_counter_only 
    counter++
    render (content.html)

@verif_required
def url_with_verif

@min_verif_required
def url_with_min_and_verif
    verif_code = 12345


#Not autodownload
def url_counter_only 
    counter++
    render (content.html)

@verif_required
def url_with_verif

@min_verif_required
def url_with_min_and_verif




[domain]/short_code




Behavior:
1. URL Link 
    - Counter only
    - No authentication

2. URL Link
    - No counter
    - Captured MIN already, send verif code via sms

3. URL Link
    - No counter
    - Must input MIN, send verif code via sms

'''
