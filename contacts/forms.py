from django import forms
from coreApp.models import Entreprise
from .models import ConditionsReglement, Client,Fournisseur,Commercial,Prospect
from accounts.models import CustomUser
from django_flatpickr.widgets import DatePickerInput

class ConditionsReglementForm(forms.ModelForm):
    class Meta:
        model = ConditionsReglement
        fields = ['typeDeReglement']

class ClientCreationForm(forms.ModelForm):
    
    entreprise = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            # Set the queryset to the user's associated entreprise
            self.fields['entreprise'].queryset = Entreprise.objects.filter(id=user.entreprise.id)
            # Set the initial value of the entreprise field
            self.fields['entreprise'].initial = user.entreprise
            # Disable the field to prevent modification
            self.fields['entreprise'].disabled = True
    
   
    date_initial_solde=forms.DateField(widget=DatePickerInput(attrs={'locale': 'fr'}),required=False)
    raison_sociale=forms.CharField(required=True)
    logo_societe = forms.ImageField(label='Logo Contact', required=False)
    pays = forms.CharField(widget=forms.Select(choices=[('Maroc', 'Maroc'), ('France', 'France'), ('Autre', 'Autre')]))
    devise = forms.CharField(widget=forms.Select(choices=[('MAD', 'MAD'), ('Euro', '€'), ('Dollar', '$')]))
    suivi_par = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        empty_label='---------',  # Adds an empty option at the beginning
        required=False,  # Make it not required if needed
        label='Suivi Par')
    
    def clean_raison_sociale(self):
        raison_sociale = self.cleaned_data.get('raison_sociale')
        if Client.objects.filter(raison_sociale=raison_sociale).exists():
            raise forms.ValidationError("La Raison sociale doit etre unique veuillez entrer un nouveau champs unique.")
        return raison_sociale

    class Meta:
        model = Client
        fields = '__all__'
        error_messages = {
            'type_societe': {
                'required': "Ce champ est requis, veuillez spécifier le type d'activité.",  
            },
        }

class SupplierCreationForm(forms.ModelForm):
    
    entreprise = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            # Set the queryset to the user's associated entreprise
            self.fields['entreprise'].queryset = Entreprise.objects.filter(id=user.entreprise.id)
            # Set the initial value of the entreprise field
            self.fields['entreprise'].initial = user.entreprise
            # Disable the field to prevent modification
            self.fields['entreprise'].disabled = True
    
   
    date_initial_solde=forms.DateField(widget=DatePickerInput(attrs={'locale': 'fr'}),required=False)
    raison_sociale=forms.CharField(required=True)
    logo_societe = forms.ImageField(label='Logo Contact', required=False)
    #type_societe=forms.CharField(required=False)
    pays = forms.CharField(widget=forms.Select(choices=[('Maroc', 'Maroc'), ('France', 'France'), ('Autre', 'Autre')]))
    devise = forms.CharField(widget=forms.Select(choices=[('MAD', 'MAD'), ('€', 'Euro'), ('$', 'Dollar')]))
    suivi_par = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        empty_label='---------',  # Adds an empty option at the beginning
        required=False,  # Make it not required if needed
        label='Suivi Par')
    
    def clean_raison_sociale(self):
        raison_sociale = self.cleaned_data.get('raison_sociale')
        if Fournisseur.objects.filter(raison_sociale=raison_sociale).exists():
            raise forms.ValidationError("La Raison sociale doit etre unique veuillez entrer un nouveau champs unique.")
        return raison_sociale

    class Meta:
        model = Fournisseur
        fields = '__all__'
        error_messages = {
            'type_societe': {
                'required': "Ce champ est requis, veuillez spécifier le type d'activité.",  
            },
        }

class ProspectCreationForm(forms.ModelForm):
    
    entreprise = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            # Set the queryset to the user's associated entreprise
            self.fields['entreprise'].queryset = Entreprise.objects.filter(id=user.entreprise.id)
            # Set the initial value of the entreprise field
            self.fields['entreprise'].initial = user.entreprise
            # Disable the field to prevent modification
            self.fields['entreprise'].disabled = True
    
   
    date_initial_solde=forms.DateField(widget=DatePickerInput(attrs={'locale': 'fr'}),required=False)
    raison_sociale=forms.CharField(required=True)
    logo_societe = forms.ImageField(label='Logo Contact', required=False)
    #type_societe=forms.CharField(required=False)
    pays = forms.CharField(widget=forms.Select(choices=[('Maroc', 'Maroc'), ('France', 'France'), ('Autre', 'Autre')]))
    devise = forms.CharField(widget=forms.Select(choices=[('MAD', 'MAD'), ('€', 'Euro'), ('$', 'Dollar')]))
    suivi_par = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        empty_label='---------',  # Adds an empty option at the beginning
        required=False,  # Make it not required if needed
        label='Suivi Par')
    
    def clean_raison_sociale(self):
        raison_sociale = self.cleaned_data.get('raison_sociale')
        if Prospect.objects.filter(raison_sociale=raison_sociale).exists():
            raise forms.ValidationError("La Raison sociale doit etre unique veuillez entrer un nouveau champs unique.")
        return raison_sociale

    class Meta:
        model = Prospect
        fields = '__all__'
        error_messages = {
            'type_societe': {
                'required': "Ce champ est requis, veuillez spécifier le type d'activité.",  
            },
        }
          
class CommercialForm(forms.ModelForm):
    entreprise = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            # Set the queryset to the user's associated entreprise
            self.fields['entreprise'].queryset = Entreprise.objects.filter(id=user.entreprise.id)
            # Set the initial value of the entreprise field
            self.fields['entreprise'].initial = user.entreprise
            # Disable the field to prevent modification
            self.fields['entreprise'].disabled = True
    class Meta:
        model = Commercial
        fields = '__all__'
        error_messages = {
            'nom': {
                'required': "Ce champ est requis, veuillez entrer le nom.",  
            },
        }