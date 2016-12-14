from django.conf.urls import url
from .views import min_verif, verif

urlpatterns = [
    url('^$', min_verif, name="min_verif"),
    url(r'^(?P<min_key>[\w-]+)/$', verif, name="verif"),
]

