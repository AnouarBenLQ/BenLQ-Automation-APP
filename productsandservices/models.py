from django.db import models
from coreApp.models import Entreprise
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

class SousCategorie(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

class Remise(models.Model):
    POURCENTAGE = 'P'
    FIXED_VALUE = 'F'

    TYPE_CHOICES = [
        (POURCENTAGE, 'Pourcentage'),
        (FIXED_VALUE, 'Valeur Fixe'),
    ]

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        if self.type == self.POURCENTAGE:
            return f"{self.value}%"
        elif self.type == self.FIXED_VALUE:
            return f"{self.value} (Fixed)"
        else:
            return "Invalid Type"
    
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
    remise_achat =  models.ForeignKey(Remise, on_delete=models.SET_NULL, null=True, blank=True)
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
    tva_pourcentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.2)
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
        