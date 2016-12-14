from __future__ import unicode_literals

from django.db import models


class Content(models.Model):
    content_name = models.CharField(max_length=64)
    content_type = models.CharField(max_length=64)
    content_file = models.FileField(upload_to='contents/', default='settings.MEDIA_ROOT/tmp/tmp.mms')
    content_dl_ctr = models.PositiveSmallIntegerField(default=0)
    timestamp  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.content_name)


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
