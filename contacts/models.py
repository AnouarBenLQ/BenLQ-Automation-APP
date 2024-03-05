from django.db import models
from coreApp.models import Entreprise
from accounts.models import CustomUser

class ConditionsReglement(models.Model):
    LABEL_CHOICES = [
        ('A_RECEPTION_FACTURE', 'À réception de la facture'),
        ('60_40_A_LA_LIVRAISON', '60% à la commande, 40% à la livraison'),
        # Add more choices as needed
    ]

    typeDeReglement = models.CharField(max_length=20, choices=LABEL_CHOICES)

    def __str__(self):
        return self.get_label_display()
    
class BaseEntity(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    TYPE = [('Societe', 'Societé'), ('Particulier', 'Particulier'), ]
    logo_societe=models.ImageField(upload_to='contacts/logos/', null=True, blank=True, verbose_name="Logo Contact")
    type_societe = models.CharField(max_length=20, choices=TYPE, default='Societe')
    raison_sociale = models.CharField(max_length=255, verbose_name="Raison sociale",unique=True)
    prenom = models.CharField(max_length=255,verbose_name="Prenom",blank=True, null=True)
    nom = models.CharField(max_length=255, verbose_name="Nom",blank=True, null=True)
    telephone = models.CharField(max_length=20, verbose_name="Téléphone",blank=True, null=True)
    adresse = models.CharField(max_length=255,verbose_name="Adresse",blank=True, null=True)
    ville = models.CharField(max_length=255, verbose_name="Ville",blank=True, null=True)
    province = models.CharField(max_length=255, verbose_name="Province",blank=True, null=True)
    code_postal = models.CharField(max_length=10, verbose_name="Code postal",blank=True, null=True)
    pays = models.CharField(max_length=255, verbose_name="Pays",blank=True, null=True)
    gsm = models.CharField(max_length=20, verbose_name="GSM",blank=True, null=True)
    fax = models.CharField(max_length=20, verbose_name="Fax",blank=True, null=True)
    email = models.EmailField(verbose_name="Adresse email",blank=True, null=True)
    site_web = models.URLField(max_length=200, blank=True, null=True, verbose_name="Site web")
    note=models.TextField(verbose_name="Informations",blank=True, null=True)
    suivi_par=models.ForeignKey(CustomUser,blank=True, null=True,on_delete=models.CASCADE, verbose_name="Suivi Par")

    banque = models.CharField(max_length=255, verbose_name="Banque",blank=True, null=True)
    RIB = models.CharField(max_length=27, verbose_name="RIB",blank=True, null=True)
    RC = models.CharField(max_length=27, verbose_name="RC- Registre de Commerce",blank=True, null=True)
    devise = models.CharField(max_length=3, default='MAD', verbose_name="Devise",blank=True, null=True)
    ICE = models.CharField(max_length=20,blank=True, null=True)
    IF = models.CharField(max_length=20,blank=True, null=True, verbose_name="Identifiant Fiscal")
    solde_initial = models.IntegerField(blank=True, null=True)
    plafond = models.IntegerField(blank=True, null=True)
    conditions_reglement = models.CharField(max_length=20, choices=ConditionsReglement.LABEL_CHOICES, null=True, blank=True)
    date_initial_solde = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.raison_sociale


class Client(BaseEntity):
    pass

class Fournisseur(BaseEntity):
    pass

class Prospect(BaseEntity):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, default=1)
    raison_sociale = models.CharField(max_length=255, verbose_name="Raison sociale",unique=True,default="Debug")
    
    pass

class Commercial(models.Model):
    
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE,default=1)
    nom = models.CharField(max_length=50,unique=True)
    prenom = models.CharField(max_length=50,)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    ville = models.CharField(max_length=50, null=True, blank=True)
    commission_pourcentage = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.prenom} {self.nom}"