from django.conf.urls import url
from .views import min_verif

urlpatterns = [
    url('^$', min_verif, name="min_verif"),
]

