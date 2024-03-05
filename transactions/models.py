from django.db import models
from coreApp.models import Entreprise
from accounts.models import CustomUser
from contacts.models import Client,Commercial
from productsandservices.models import Remise

# Create your models here.*
class BaseDevis(models.Model):
    
    STATUS_CHOICES = [
        ('encours', 'En cours'),
        ('expire', 'Éxpiré'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('paye', 'Payé'),
    ]
    
    
    status_devis = models.CharField(max_length=20, choices=STATUS_CHOICES, default='encours')
    date = models.DateTimeField(auto_now_add=True)
    date_modification =  models.DateTimeField(auto_now=True)
    echeance = models.DateTimeField()
    reference = models.CharField(max_length=100,blank=True,null=True)
    type_devis = models.CharField(max_length=10, choices=[('achat', 'Achat'), ('vente', 'Vente')])
    objet = models.CharField(max_length=100,blank=True,null=True)
    commission_pourcentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0,null=True, blank=True)
    remise = models.ForeignKey(Remise, on_delete=models.SET_NULL, null=True, blank=True)
    adresse_de_livraison = models.CharField(max_length=100,blank=True,null=True)
    delai_livraison = models.CharField(max_length=100,blank=True,null=True)
    condition_livraison = models.CharField(max_length=100,blank=True,null=True)
    note=models.TextField()
    
    class Meta:
        abstract = True

class BaseLigne(models.Model):
    
    reference = models.CharField(max_length=100,blank=True,null=True,unique=True)
    designation = models.CharField(max_length=100)
    quantite = models.PositiveIntegerField(default=1)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=0.2)
    montant_tva = models.DecimalField(max_digits=10, decimal_places=3)
    montant_ht = models.DecimalField(max_digits=10, decimal_places=3)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=3)
    remise = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    class Meta:
        abstract = True

    
    def save(self, *args, **kwargs):
        # Set default value for echeance 1 month later than the date
        if self.montant_ttc is None:
            self.montant_ttc = self.montant_ht * (1 + self.tva)  # Calculate montant_ttc if not provided
        if self.montant_tva is None:
            self.montant_tva = self.tva * self.montant_ht

        super().save(*args, **kwargs)

    
        
class Devis(BaseDevis):
    
    numero = models.AutoField(primary_key=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='devis_vente')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='devis_suivi_par')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devis_clients', null=False, blank=True)
    commercial = models.ForeignKey(Commercial, on_delete=models.CASCADE,null=True, blank=True, related_name='commercial_devis_vente')
    document = models.FileField(upload_to='documents/devisdevente/')
    bon_de_commande = models.ForeignKey("Commande", on_delete=models.SET_NULL, null=True, blank=True, related_name='bon_de_commande')
    

class LigneDevis(BaseLigne):
    devis = models.ForeignKey(Devis, on_delete=models.CASCADE, related_name='lignes_devis')
    
class Commande(BaseDevis):
    
    numero = models.AutoField(primary_key=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='commande')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='commandes_suivi_par')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commande_clients', null=False, blank=True)
    commercial = models.ForeignKey(Commercial, on_delete=models.CASCADE,null=True, blank=True, related_name='commercial_commande_vente')
    document = models.FileField(upload_to='documents/bondecommande/')
    bon_de_livraison = models.ForeignKey("Livraison", on_delete=models.SET_NULL, null=True, blank=True, related_name='bon_de_livraison')

class LigneCommande(BaseLigne):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes_commande')

class Livraison(BaseDevis):
    
    numero = models.AutoField(primary_key=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='livraisons')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='livraisons_suivi_par')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='livraison_clients', null=False, blank=True)
    commercial = models.ForeignKey(Commercial, on_delete=models.CASCADE,null=True, blank=True, related_name='commercial_livraison_vente')
    document = models.FileField(upload_to='documents/bondelivraison/')
    facture = models.ForeignKey("Facture", on_delete=models.SET_NULL, null=True, blank=True, related_name='facture')

class LigneLivraison(BaseLigne):
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE, related_name='lignes_livraison')

class Facture(BaseDevis):
    
    numero = models.AutoField(primary_key=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='factures')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='factures_suivi_par')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='facture_clients', null=False, blank=True)
    commercial = models.ForeignKey(Commercial, on_delete=models.CASCADE,null=True, blank=True, related_name='commercial_facture_vente')
    document = models.FileField(upload_to='documents/factures/')

class LigneFacture(BaseLigne):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes_facture')
    marge_beneficiaire= models.DecimalField(max_digits=10, decimal_places=3)

class Retour(BaseDevis):
    
    numero = models.AutoField(primary_key=True)
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='retours_suivi_par')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='retour_clients', null=False, blank=True)
    document = models.FileField(upload_to='documents/bonderetour/')

class LigneRetour(BaseLigne):
    
    facture = models.ForeignKey(Retour, on_delete=models.CASCADE, related_name='lignes_retour')
    
class Avoirs(BaseDevis):
    
    numero = models.AutoField(primary_key=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='avoirs')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='avoirs_suivi_par')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='avoirs_clients', null=False, blank=True)
    document = models.FileField(upload_to='documents/bonavoirs/')

class LigneAvoirs(BaseLigne):
    
    avoir = models.ForeignKey(Avoirs, on_delete=models.CASCADE, related_name='lignes_avoirs')
    
class Sales(models.Model):
    devis = models.ForeignKey(Devis, on_delete=models.CASCADE, related_name='devis_vente')
    commandes = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='commandes_vente')
    livraisons = models.ForeignKey(Livraison, on_delete=models.CASCADE, related_name='livraisons_vente')
    factures = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='factures_vente')
    retours = models.ForeignKey(Retour, on_delete=models.CASCADE, related_name='retours_vente')
    avoirs = models.ForeignKey(Avoirs, on_delete=models.CASCADE, related_name='avoirs_vente')
    
class Purchases(models.Model):
    pass
