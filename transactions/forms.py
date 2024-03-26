from django import forms
from .models import Devis
from contacts.models import Client
from coreApp.models import Entreprise
from datetime import date,datetime, timedelta
from django import forms


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

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date')
    echeance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Echeance')

    class Meta:
        model = Devis
        fields = ['numero', 'suivi_par', 'client', 'commercial', 'date', 'echeance']
        