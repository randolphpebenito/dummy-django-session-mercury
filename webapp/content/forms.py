from django import forms


class MsisdnForm(forms.Form):
    msisdn = forms.CharField(label='', max_length=100)
