from django.db import models
from coreApp.models import Entreprise

class ConditionsReglement(models.Model):
    LABEL_CHOICES = [
        ('A_RECEPTION_FACTURE', 'À réception de la facture'),
        ('60_40_A_LA_LIVRAISON', '60% à la commande, 40% à la livraison'),
        # Add more choices as needed
    ]

    label = models.CharField(max_length=20, choices=LABEL_CHOICES)

    def __str__(self):
        return self.get_label_display()
    
class BaseEntity(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    TYPE = [('Societe', 'Societé'), ('Particulier', 'Particulier'), ]
    type_societe = models.CharField(max_length=20, choices=TYPE, default='Societe')
    raison_sociale = models.CharField(max_length=255, verbose_name="Raison sociale")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    adresse = models.TextField(verbose_name="Adresse")
    ville = models.CharField(max_length=255, verbose_name="Ville")
    code_postal = models.CharField(max_length=10, verbose_name="Code postal")
    pays = models.CharField(max_length=255, verbose_name="Pays")
    gsm = models.CharField(max_length=20, verbose_name="GSM")
    fax = models.CharField(max_length=20, verbose_name="Fax")
    email = models.EmailField(verbose_name="Adresse email")
    site_web = models.URLField(max_length=200, blank=True, null=True, verbose_name="Site web")

    banque = models.CharField(max_length=255, verbose_name="Banque")
    RIB = models.CharField(max_length=27, verbose_name="RIB")
    RC = models.CharField(max_length=27, verbose_name="RC- Registre de Commerce")
    devise = models.CharField(max_length=3, default='MAD', verbose_name="Devise")
    ICE = models.CharField(max_length=20)
    IF = models.CharField(max_length=20, verbose_name="Identifiant Fiscal")
    solde_initial = models.DecimalField(max_digits=10, decimal_places=2)
    plafond = models.DecimalField(max_digits=10, decimal_places=2)
    conditions_reglement = models.ForeignKey(ConditionsReglement, on_delete=models.SET_NULL, null=True, blank=True)
    date_initial_solde = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.raison_sociale


class Client(BaseEntity):
    pass

class Fournisseur(BaseEntity):
    pass

class Prospect(models.Model):
    pass

class Commercial(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    ville = models.CharField(max_length=50, null=True, blank=True)
    commission_pourcentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.prenom} {self.nom}"