import re
from django import forms
from django.contrib.auth.models import User

FMT_MSISDN_REGEX = re.compile("""^09\d{9}$""")

class MsisdnForm(forms.Form):
    #msisdn = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'e.g 09xxxxxxxxx'}))
    msisdn = forms.CharField(label='', max_length=100, 
            widget=forms.TextInput(attrs={
                'placeholder': 'e.g 09xxxxxxxxx',
                'class': 'form-control',
                #type="email" class="form-control" id="exampleInputEmail1" placeholder="e.g. 09xxxxxxxxx"
            }))

    def clean_msisdn(self):
        msisdn = self.cleaned_data['msisdn']

        #Ensure msisdn is 09xxxxxxxxx
        if FMT_MSISDN_REGEX.match(msisdn) is None:
            raise forms.ValidationError("Invalid MSISDN!")

        return msisdn

    def save(self, commit=True):
        msisdn = self.cleaned_data['msisdn']
        try:
            user_msisdn = User.objects.get(username=msisdn)
        except User.DoesNotExist:
            user_msisdn = User.objects.create_user(
                username=msisdn,
                password='12345',
            )

        return user_msisdn 

class MsisdnVerifForm(forms.Form):
    verif = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={
            'placeholder': 'e.g 12345',
            'class': 'form-control',
        }))

