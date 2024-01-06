from django.db import models
from django.contrib.auth.models import AbstractUser
from coreApp.models import Entreprise
# Create your models here.


# Create your models here.

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    status = models.BooleanField(default=True, verbose_name="Statut actif/non actif")
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='comptables', verbose_name="Entreprise")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)