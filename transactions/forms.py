from django import forms
from .models import Devis
from contacts.models import Client
from coreApp.models import Entreprise
from datetime import date,datetime, timedelta
from django import forms
from accounts.models import CustomUser


class DevisForm(forms.ModelForm):
    
    
    class Meta:
        model = Devis
        fields = '__all__'
        

class DevisClient(forms.Form):
    
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label='Date',initial=date.today)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client')

class InformationDevis(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InformationDevis, self).__init__(*args, **kwargs)
        # Set initial values for date and echeance
        self.fields['date'].initial = date.today()
        self.fields['echeance'].initial = date.today() + timedelta(days=30)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client',
                                    widget=forms.Select(attrs={'class': 'w-1/2 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}),)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}), label='Date')
    echeance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}), label="Valable jusqu'au")
    reference = forms.CharField(widget=forms.DateInput(attrs={'type': 'text','class':'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}), label="Réference")
    suivi_par = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='Suivi Par',
                                    widget=forms.Select(attrs={'class': 'w-1/2 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}),)
    class Meta:
        model = Devis
        fields = ['numero', 'suivi_par', 'client','reference', 'commercial', 'date', 'echeance',]
        