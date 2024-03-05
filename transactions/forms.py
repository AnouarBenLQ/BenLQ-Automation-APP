from django import forms
from .models import Devis

class DevisForm(forms.ModelForm):
    
    
    class Meta:
        model = Devis
        fields = '__all__'