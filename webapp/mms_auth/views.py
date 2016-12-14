import random, string

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import MsisdnForm, MsisdnVerifForm
from .models import MsisdnUrl



# Create your views here.
def min_verif(request):
    if request.method == "POST":      
        form = MsisdnForm(request.POST)
        if form.is_valid():
            msisdn = form.cleaned_data['msisdn']

            f_msisdn = form.save()
            msisdn_key = ''
            try:
                mu = MsisdnUrl.objects.get(msisdn=f_msisdn)
                msisdn_key = mu.short_code

            except MsisdnUrl.DoesNotExist:
                msisdn_key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5)) 
                MsisdnUrl.objects.create(msisdn=f_msisdn, short_code=msisdn_key)

            return HttpResponseRedirect("/auth/%s/" % msisdn_key)
    else:
        form = MsisdnForm()

    return render(request, 'auth/min_verif.html', {'form': form})
    

def verif(request, min_key):
    try:
        m = MsisdnUrl.objects.get(short_code=min_key)
    except MsisdnUrl.DoesNotExist:
        return HttpResponseRedirect("/auth/")

    if request.method == "POST":      
        form = MsisdnVerifForm(request.POST)
        if form.is_valid():
            verif = form.cleaned_data['verif']
            user = authenticate(username=m.msisdn.username, password=verif)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/m/%s/" % min_key)
     
            else:
                return render(request, 'auth/min_verif_challenge.html', {'form': form, 'invalid_verif': True})
    else:
        form = MsisdnVerifForm()

    return render(request, 'auth/min_verif_challenge.html', {'form': form})
    
