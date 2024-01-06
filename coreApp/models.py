from django.db import models
from django.utils import timezone

# Create your models here.

class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=255, verbose_name="Raison sociale")
    email = models.EmailField(verbose_name="Adresse email")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    adresse = models.TextField(verbose_name="Adresse")
    ville = models.CharField(max_length=255, verbose_name="Ville")
    code_postal = models.CharField(max_length=10, verbose_name="Code postal")
    informations_fiscales = models.TextField(verbose_name="Informations fiscales")
    site_web = models.URLField(max_length=200, blank=True, null=True,verbose_name="Informations fiscales")
    logo = models.ImageField(upload_to='logo/', null=True, blank=True, verbose_name="Logo de l'entreprise")
    cachet_signature = models.ImageField(upload_to='cachet/', null=True, blank=True, verbose_name="Cachet de signature")
    
    def __str__(self):
        return self.raison_sociale
    