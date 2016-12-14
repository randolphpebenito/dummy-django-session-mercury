import random, string

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from mms_auth.models import MsisdnUrl
from .models import Content 
    
def min_verif_home(request, code):
    
    if request.user.is_authenticated():
        try:
            MsisdnUrl.objects.get(msisdn=request.user, short_code=code)
        except MsisdnUrl.DoesNotExist:
            return HttpResponseRedirect('/auth/')

	c = Content.objects.all()

	return render(request, 'content/min_verif_home.html', { 'mms': c[0] })
    else:
        return HttpResponseRedirect('/auth/')

def min_verif_home_auto_dl(request, code):
    
    if request.user.is_authenticated():
        try:
            MsisdnUrl.objects.get(msisdn=request.user, short_code=code)
        except MsisdnUrl.DoesNotExist:
            return HttpResponseRedirect('/auth/')

	return render(request, 'content/min_verif_home_auto_dl.html')
    else:
        return HttpResponseRedirect('/auth/')

def content_list(request, code):
    return render(request, 'content/list.html')



def min_verif_home_logout(request):
    logout(request)
    return HttpResponseRedirect('/auth/')

