from django import forms
from coreApp.models import Entreprise
from .models import Produit,Service,PackProduct,Categorie,SousCategorie,Promotion
from accounts.models import CustomUser
from colorfield.fields import ColorField


class ProductForm(forms.ModelForm):
    entreprise = forms.ModelChoiceField(queryset=None)
    couleur = ColorField()
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
        model = Produit
        fields = '__all__'
        error_messages = {
            'nom': {
                'required': "Ce champ est requis, veuillez entrer le nom.",  
            },
        }

class ServiceForm(forms.ModelForm):
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
        model = Service
        fields = '__all__'
        error_messages = {
            'nom': {
                'required': "Ce champ est requis, veuillez entrer le nom.",  
            },
        }
    
class PackProductForm(forms.ModelForm):
    new_pack_name = forms.CharField(max_length=50, label='Nouveau Pack produit')
    product = forms.ModelChoiceField(queryset=Produit.objects.all(), label='Produit')

    
    class Meta:
        model = PackProduct
        fields = ['new_pack_name', 'product', 'quantity']
        
class CategoryForm(forms.ModelForm):
    nom = forms.CharField(max_length=50, label='Label Catégorie')
    class Meta:
        model = Categorie
        fields = ['nom']
        
class SubcategoryForm(forms.ModelForm):
    nom = forms.CharField(max_length=50, label='Label Sous-catégorie')
    category = forms.ModelChoiceField(queryset=Categorie.objects.all(), label='Catégorie associée')

    
    class Meta:
        model = SousCategorie
        fields = ['nom', 'category']

class PromotionForm(forms.ModelForm):
    date_debut=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label='Date début')
    date_fin=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label='Date fin')
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), label='Produit')
    taux_reduction=forms.DecimalField(label="Taux réduction (%)")
    
    class Meta:
        model = Promotion
        fields = ['nom','produit', 'taux_reduction','date_debut','date_fin']