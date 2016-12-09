import base64
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import MsisdnForm



# Create your views here.
def min_verif(request):
    form = MsisdnForm()
    if request.method == "POST":      
        form = MsisdnForm(request.POST)
        if form.is_valid():
            msisdn = form.cleaned_data['msisdn']
            User.objects.create_user(
                username=msisdn,
                password='12345',
            )
            msisdn_key = base64.urlsafe_b64encode(msisdn)
        return HttpResponseRedirect("/mms/%s/" % msisdn_key)
    return render(request, 'base.html', {'form': form})
    

def verif(request, min_key):
    msisdn = base64.urlsafe_b64decode(min_key)
    return HttpResponse(msisdn)
    
