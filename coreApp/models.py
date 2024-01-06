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
    

class Devis(models.Model):
    
    STATUS_CHOICES = [
        ('encours', 'En cours'),
        ('expire', 'Éxpiré'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('paye', 'Payé'),
    ]
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='devis')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='devis_suivi_par')
    status_devis = models.CharField(max_length=20, choices=STATUS_CHOICES, default='encours')
    date = models.DateTimeField(auto_now_add=True)
    date_modification =  models.DateTimeField(auto_now=True)
    echeance = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=50, unique=True)
    document = models.FileField(upload_to='documents/devisdevente/')
    montant_total_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    bon_de_commande = models.ForeignKey("Commande", on_delete=models.SET_NULL, null=True, blank=True, related_name='bon_de_commande')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devis_clients', null=True, blank=True)
   
    
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
    devis = models.ForeignKey(Devis_Vente, on_delete=models.CASCADE, related_name='lignes_devis')
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

class Commande(models.Model):
     
    STATUS_CHOICES = [
        ('encours', 'En cours'),
        ('expire', 'Éxpiré'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('paye', 'Payé'),
    ]
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='commandes')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='devis_suivi_par')
    status_devis = models.CharField(max_length=20, choices=STATUS_CHOICES, default='encours')
    date = models.DateTimeField(auto_now_add=True)
    date_modification =  models.DateTimeField(auto_now=True)
    echeance = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=50, unique=True)
    document = models.FileField(upload_to='documents/bonsdecommande/')
    montant_total_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type_devis = models.CharField(max_length=10, choices=[('achat', 'Achat'), ('vente', 'Vente')])
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devis_clients', null=True, blank=True)
    bon_de_livraison = models.ForeignKey('Livraison', on_delete=models.SET_NULL, null=True, blank=True, related_name='bon_de_livraison')

   
    
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
    
class LigneCommande(models.Model):
    commande = models.ForeignKey("Commande", on_delete=models.CASCADE, related_name='lignes_commandes')
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

class Livraison(models.Model):
    STATUS_CHOICES = [
        ('encours', 'En cours'),
        ('expire', 'Éxpiré'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('paye', 'Payé'),
    ]
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='commandes')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='devis_suivi_par')
    status_devis = models.CharField(max_length=20, choices=STATUS_CHOICES, default='encours')
    date = models.DateTimeField(auto_now_add=True)
    date_modification =  models.DateTimeField(auto_now=True)
    echeance = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=50, unique=True)
    document = models.FileField(upload_to='documents/bonsdelivraison/')
    montant_total_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type_devis = models.CharField(max_length=10, choices=[('achat', 'Achat'), ('vente', 'Vente')])
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devis_clients', null=True, blank=True)
    facture = models.ForeignKey('Facture', on_delete=models.SET_NULL, null=True, blank=True, related_name='facture')
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
     
class LigneLivraison(models.Model):
    livraison = models.ForeignKey("Livraison", on_delete=models.CASCADE, related_name='lignes_livraison')
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

class Facture(models.Model):
    STATUS_CHOICES = [
        ('encours', 'En cours'),
        ('expire', 'Éxpiré'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('paye', 'Payé'),
    ]
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='commandes')
    suivi_par = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='devis_suivi_par')
    status_devis = models.CharField(max_length=20, choices=STATUS_CHOICES, default='encours')
    date = models.DateTimeField(auto_now_add=True)
    date_modification =  models.DateTimeField(auto_now=True)
    echeance = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=50, unique=True)
    document = models.FileField(upload_to='documents/facture/')
    montant_total_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type_devis = models.CharField(max_length=10, choices=[('achat', 'Achat'), ('vente', 'Vente')])
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devis_clients', null=True, blank=True)
    bénefice= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
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
     
class LigneFacture(models.Model):
    facture = models.ForeignKey("Facture", on_delete=models.CASCADE, related_name='lignes_facture')
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