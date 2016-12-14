"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url, static
from django.views.static import serve
from django.contrib import admin

from content.views import (
    min_verif_home, 
    min_verif_home_auto_dl, 
    min_verif_home_logout,
    content_list,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^m/logout/$', min_verif_home_logout, name="min_verif_home_logout"),
    url(r'^m/(?P<code>[\w-]+)/$', min_verif_home, name="min_verif_home"),
    url(r'^m/(?P<code>[\w-]+)/list/$', content_list, name="content_list"),
    url(r'^m/dl/(?P<code>[\w-]+)/$', min_verif_home_auto_dl, name="min_verif_home_auto_dl"),
    url(r'^auth/', include('mms_auth.urls')),
]

#if settings.DEBUG is True:
#    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

