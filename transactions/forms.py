from django import forms
from .models import Devis
from contacts.models import Client
from datetime import date

class DevisForm(forms.ModelForm):
    
    
    class Meta:
        model = Devis
        fields = '__all__'
        

class DevisClient(forms.ModelForm):
    
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label='Date',initial=date.today)
    produit = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client')