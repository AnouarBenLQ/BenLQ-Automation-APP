from django import forms
from .models import Devis
from productsandservices.models import Remise
from contacts.models import Client,Commercial
from coreApp.models import Entreprise
from datetime import date,datetime, timedelta
from django import forms
from accounts.models import CustomUser



class RemiseForm(forms.ModelForm):
    class Meta:
        model = Remise
        fields = ['type_remise', 'value']
        
class DevisForm(forms.ModelForm):
    
    
    class Meta:
        model = Devis
        fields = '__all__'
        

class DevisClient(forms.Form):
    
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label='Date',initial=date.today)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client')

class InformationDevis(forms.ModelForm):

    
             
            
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client',
                                    widget=forms.Select(attrs={'class': 'w-1/2 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}),)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}), label='Date')
    echeance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}), label="Valable jusqu'au")
    reference = forms.CharField(widget=forms.TextInput(attrs={'type': 'text','class':'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}), label="Réference")
    numero = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'number','min':'1','class':'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}), label="Numéro")
    suivi_par = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='Suivi Par',
                                    widget=forms.Select(attrs={'class': 'w-1/2 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}),)
    class Meta:
        model = Devis
        fields = ['numero', 'suivi_par', 'client','reference', 'commercial', 'date', 'echeance',]
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super(InformationDevis, self).__init__(*args, **kwargs)
        
        # Set initial values for date and echeance
        
        last_item = Devis.objects.all().order_by('numero').last()
        next_number = (last_item.numero + 1) if last_item else 1
        self.fields['numero'].initial = next_number
        self.fields['date'].initial = date.today()
        self.fields['echeance'].initial = date.today() + timedelta(days=30)
        self.fields['reference'].initial = 'Aucune'
        
        if user and user.is_authenticated:
            self.fields['suivi_par'].initial = user  # Set the initial value to the authenticated user
            
class ConditiondeVente(forms.ModelForm):
    commercial = forms.ModelChoiceField(queryset=Commercial.objects.all(), label='Commercial',
                                    widget=forms.Select(attrs={'class': 'w-1/2 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'}),)
    
    
    
    
    class Meta:
        model=Devis
        fields=['commercial','commission_pourcentage','type_remise','valeur_remise','devise','moyen_de_paiement','condition_reglement','adresse_de_livraison','date_livraison','condition_livraison','note']