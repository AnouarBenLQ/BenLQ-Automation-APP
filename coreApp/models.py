from django.db import models
from django.utils import timezone

# Create your models here.

class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=255, verbose_name="Raison sociale",)
    email = models.EmailField(verbose_name="Adresse email",null=True,blank=True)
    telephone = models.CharField(max_length=20, verbose_name="Téléphone",null=True,blank=True)
    adresse = models.TextField(verbose_name="Adresse",null=True,blank=True)
    ville = models.CharField(max_length=255, verbose_name="Ville",null=True,blank=True)
    code_postal = models.CharField(max_length=10, verbose_name="Code postal",null=True,blank=True)
    informations_fiscales = models.TextField(verbose_name="Informations fiscales",null=True,blank=True)
    site_web = models.URLField(max_length=200, blank=True, null=True,verbose_name="Site Web",)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True, verbose_name="Logo de l'entreprise")
    cachet_signature = models.ImageField(upload_to='cachet/', null=True, blank=True, verbose_name="Cachet de signature")
    
    def __str__(self):
        return self.raison_sociale
    