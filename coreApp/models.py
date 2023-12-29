from django.db import models
from django.utils import timezone
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
    
class Prospect(models.Model):
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
    
class Commercial(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    ville = models.CharField(max_length=50, null=True, blank=True)
    commission_pourcentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class Categorie(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

class SousCategorie(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom
    
class Produit(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='produits')
    reference = models.CharField(max_length=50, unique=True)
    code_barre = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=255)
    pays_dorigine = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    sous_categorie = models.ForeignKey(SousCategorie, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    emplacement = models.CharField(max_length=50, null=True, blank=True)
    sur_catalog = models.BooleanField(default=False)
    prix_1 = models.DecimalField(max_digits=10, decimal_places=2)
    prix_ttc_1 = models.DecimalField(max_digits=10, decimal_places=2)
    prix_2 = models.DecimalField(max_digits=10, decimal_places=2)
    prix_ttc_2 = models.DecimalField(max_digits=10, decimal_places=2)
    prix_3 = models.DecimalField(max_digits=10, decimal_places=2)
    prix_ttc_3 = models.DecimalField(max_digits=10, decimal_places=2)
    prix_achat_net = models.DecimalField(max_digits=10, decimal_places=2)
    prix_achat_net_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    remise_achat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    prix_achat_brut = models.DecimalField(max_digits=10, decimal_places=2)
    prix_achat_brut_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    image_produit = models.ImageField(upload_to='produit/', null=True, blank=True)
    tva_pourcentage = models.DecimalField(max_digits=5, decimal_places=2)
    largeur = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    longueur = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    epaisseur = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    unite_principale = models.CharField(max_length=20, null=True, blank=True)
    unite_vente = models.CharField(max_length=20, null=True, blank=True)
    marque = models.CharField(max_length=50, null=True, blank=True)
    couleur = models.CharField(max_length=50, null=True, blank=True)
    taille = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.reference} - {self.designation}"
    
class Service(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='services')
    reference = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=255)
    pays_dorigine = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    prix_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    prix_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    prix_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    tva_pourcentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    prix_ttc_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    prix_ttc_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    prix_ttc_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    prix_achat_net = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    prix_achat_pourcentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    remise_achat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.reference} - {self.designation}"

class Pack(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    produits = models.ManyToManyField('Produit', related_name='packs')
    
    def __str__(self):
        return self.nom
    
class Promotion(models.Model):
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE, null=True, blank=True)
    pack = models.ForeignKey('Pack', on_delete=models.CASCADE, null=True, blank=True)
    taux_reduction = models.DecimalField(max_digits=5, decimal_places=2)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Promotion {self.id}"

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"


class Devis(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='clients')
    STATUS_CHOICES = [
        ('encours', 'En cours'),
        ('echu', 'Échu'),
        ('valide', 'Validé'),
    ]
    status_devis = models.CharField(max_length=20, choices=STATUS_CHOICES, default='encours')
    date = models.DateTimeField(auto_now_add=True)
    echeance = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=50, unique=True)
    document = models.FileField(upload_to='documents/')
    montant_total_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        # Set default value for echeance 1 month later than the date
        if not self.echeance:
            self.echeance = self.date + timezone.timedelta(days=30)
        self.montant_total_ttc = self.calculate_montant_total_ttc()

        super().save(*args, **kwargs)
    
    def calculate_montant_total_ttc(self):
        # Calculate the total TTC amount based on all related LigneDevis instances
        lignes_devis = self.lignes_devis.all()
        total_ttc = sum(ligne.montant_ttc for ligne in lignes_devis)
        return total_ttc

class LigneDevis(models.Model):
    devis = models.ForeignKey(Devis, on_delete=models.CASCADE, related_name='lignes_devis')
    designation = models.CharField(max_length=100)
    quantite = models.PositiveIntegerField(default=1)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=0.2)
    montant_tva = models.DecimalField(max_digits=10, decimal_places=3)
    montant_ht = models.DecimalField(max_digits=10, decimal_places=3)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=3)
    remise = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Set default value for echeance 1 month later than the date
        if self.montant_ttc is None:
            self.montant_ttc = self.montant_ht * (1 + self.tva)  # Calculate montant_ttc if not provided
        if self.montant_total_ttc is None:
            self.montant_total_ttc = self.quantite * self.montant_ttc
        if self.montant_tva is None:
            self.montant_tva = self.tva * self.montant_ht

        super().save(*args, **kwargs)