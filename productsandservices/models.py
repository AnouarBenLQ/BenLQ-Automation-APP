from django.db import models
from coreApp.models import Entreprise
from taggit.managers import TaggableManager

from decimal import Decimal
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

class SousCategorie(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)

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
    reference = models.CharField(max_length=50, unique=True,blank=True, null=True)
    code_barre = models.CharField(max_length=50, unique=True,blank=True, null=True)
    designation = models.CharField(max_length=255,unique=True,verbose_name="Désignation")
    pays_dorigine = models.CharField(max_length=255,blank=True, null=True,verbose_name="Pays d'origine")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,blank=True, null=True)
    sous_categorie = models.ForeignKey(SousCategorie, on_delete=models.CASCADE,blank=True, null=True)
    stock = models.PositiveIntegerField(default=1,verbose_name="Quantité sur stock")
    emplacement = models.CharField(max_length=50, null=True, blank=True)
    sur_catalog = models.BooleanField(default=False,blank=True, null=True)
    prix_1 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Prix de Vente HT")
    prix_ttc_1 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Prix de Vente TTC")
    prix_2 = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,verbose_name="Prix de Vente-2 HT")
    prix_ttc_2 = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,verbose_name="Prix de Vente TTC-2")
    prix_3 = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,verbose_name="Prix de Vente-3 HT")
    prix_ttc_3 = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,verbose_name="Prix de Vente TTC-3")
    prix_achat_net = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Prix d'achat HT")
    prix_achat_net_ttc = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Prix d'achat TTC")
    remise_achat =  models.ForeignKey(Remise, on_delete=models.SET_NULL, null=True, blank=True)
    prix_achat_brut = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    prix_achat_brut_ttc = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    image_produit = models.ImageField(upload_to='produit/', null=True, blank=True,default='produit/default_product.jpg')
    tva_pourcentage = models.PositiveIntegerField(default=20,verbose_name="TVA (%)")
    largeur = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    longueur = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    epaisseur = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tags = TaggableManager(blank=True)
    unite_vente = models.CharField(max_length=20, choices=(
       ('Kilogram', 'Kg'),
        ('Gram', 'g'),
        ('Pound', 'lb'),
        ('Ounce', 'oz'),
        ('Liter', 'l'),
        ('Milliliter', 'ml'),
        ('Gallon', 'gal'),
        ('Quart', 'qt'),
        ('Pack', 'pack'),
        ('Box', 'box'),
        ('Unit', 'U'),
        ('Other', 'autre'),
    ),verbose_name="Unité de vente",default="Unit")
    # unite_vente = models.CharField(max_length=20, null=True, blank=True)
    marque = models.CharField(max_length=50, null=True, blank=True)
    couleur = models.CharField(default="#7F00FF",max_length=50, null=True, blank=True)
    taille = models.CharField(max_length=50, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.reference:
            # Get the count of existing instances and increment by 1
            count = Produit.objects.count() + 1
            # Generate the reference string
            self.reference = f'REF-P {count:03d}'  # This formats the number with leading zeros
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference} - {self.designation}"
    
class Service(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='services')
    reference = models.CharField(max_length=50, unique=True,blank=True, null=True)
    designation = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=True, blank=True)
    prix_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,verbose_name="Frais du service (Prix Principal)")
    prix_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,null=True, blank=True)
    prix_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,null=True, blank=True)
    tva_pourcentage = models.PositiveIntegerField(default=20,verbose_name="TVA (%)")
    prix_ttc_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,editable = False)
    prix_ttc_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,null=True, blank=True)
    prix_ttc_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,null=True, blank=True)
    remise = models.DecimalField(max_digits=5, decimal_places=2,default=0.0,null=True, blank=True)

    def __str__(self):
        return f"{self.reference} - {self.designation}"
    
    def save(self, *args, **kwargs):
        self.prix_ttc_1 = self.prix_1 * Decimal((1 + self.tva_pourcentage / 100))
        super().save(*args, **kwargs)
        if not self.reference:
            # Get the count of existing instances and increment by 1
            count = Service.objects.count() + 1
            # Generate the reference string
            self.reference = f'REF-S {count:03d}'  # This formats the number with leading zeros
        super().save(*args, **kwargs)

class Pack(models.Model):
    nom = models.CharField(max_length=50,unique=True,)
    def __str__(self):
        return self.nom
    
class PackProduct(models.Model):
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE,verbose_name="Produit")
    quantity = models.PositiveIntegerField(verbose_name="Quantité")
    
class Promotion(models.Model):
    
    nom = models.CharField(max_length=50, unique=True)
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
        