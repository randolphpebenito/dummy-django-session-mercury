from django.conf.urls import url
from .views import min_verif, verif

urlpatterns = [
    url('^$', min_verif, name="min_verif"),
    url(r'^(?P<min_key>[0-9a-z-]+)/$', verif, name="verif"),
  #  url(r'^123/$', verif, name="verif"),
]

