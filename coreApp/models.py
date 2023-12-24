from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    status = models.BooleanField(default=True, verbose_name="Statut actif/non actif")
    entreprise = models.ForeignKey('Entreprise', on_delete=models.CASCADE, related_name='comptables', verbose_name="Entreprise")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
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

class Client(models.Model):
    
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    TYPE = [('Societe', 'Societé'),('Particulier', 'Particulier'),]
    type_societe = models.CharField(max_length=20,choices=TYPE,default='Societe')
    raison_sociale = models.CharField(max_length=255, verbose_name="Raison sociale")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    adresse = models.TextField(verbose_name="Adresse")
    ville = models.CharField(max_length=255, verbose_name="Ville")
    code_postal = models.CharField(max_length=10, verbose_name="Code postal")
    pays= models.CharField(max_length=255, verbose_name="Pays")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    gsm = models.CharField(max_length=20, verbose_name="GSM")
    fax = models.CharField(max_length=20, verbose_name="Fax")
    email = models.EmailField(verbose_name="Adresse email")
    site_web = models.URLField(max_length=200, blank=True, null=True)
    
    banque = models.CharField(max_length=255, verbose_name="Banque")
    RIB= models.CharField(max_length=27, verbose_name="RIB")
    RC=models.CharField(max_length=27, verbose_name="RC- Registre de Commerce")
    devise = models.CharField(max_length=3, default='MAD', verbose_name="Devise")
    ICE = models.CharField(max_length=20)
    IF = models.CharField(max_length=20,verbose_name="Identifiant Fiscal")
    solde_initial = models.DecimalField(max_digits=10, decimal_places=2)
    plafond = models.DecimalField(max_digits=10, decimal_places=2)
    condition_de_reglement = models.CharField(max_length=20,default="à la livraison")
    date_initial_solde = models.DateField()

    def __str__(self):
        return self.raison_sociale

class Fournisseur(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    TYPE = [('Societe', 'Societé'),('Particulier', 'Particulier'),]
    type_societe = models.CharField(max_length=20,choices=TYPE,default='Societe')
    raison_sociale = models.CharField(max_length=255, verbose_name="Raison sociale")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    adresse = models.TextField(verbose_name="Adresse")
    ville = models.CharField(max_length=255, verbose_name="Ville")
    code_postal = models.CharField(max_length=10, verbose_name="Code postal")
    pays= models.CharField(max_length=255, verbose_name="Pays")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    gsm = models.CharField(max_length=20, verbose_name="GSM")
    fax = models.CharField(max_length=20, verbose_name="Fax")
    email = models.EmailField(verbose_name="Adresse email")
    site_web = models.URLField(max_length=200, blank=True, null=True)
    
    banque = models.CharField(max_length=255, verbose_name="Banque")
    RIB= models.CharField(max_length=27, verbose_name="RIB")
    RC=models.CharField(max_length=27, verbose_name="RC- Registre de Commerce")
    devise = models.CharField(max_length=3, default='MAD', verbose_name="Devise")
    ICE = models.CharField(max_length=20)
    IF = models.CharField(max_length=20,verbose_name="Identifiant Fiscal")
    solde_initial = models.DecimalField(max_digits=10, decimal_places=2)
    plafond = models.DecimalField(max_digits=10, decimal_places=2)
    condition_de_reglement = models.CharField(max_length=20,default="à la livraison")
    date_initial_solde = models.DateField()

    def __str__(self):
        return self.raison_sociale