from django.db import models
from django.contrib.auth.models import AbstractUser
from coreApp.models import Entreprise
# Create your models here.


# Create your models here.

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=20, verbose_name="Téléphone",null=True, blank= True)
    email=models.EmailField(max_length=100,unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]
    profileImage=models.ImageField(upload_to='profileImages/', null=True, blank=True, verbose_name="Image de Profile")
    status = models.BooleanField(default=True, verbose_name="Statut actif/non actif")
    entreprise = models.ForeignKey(Entreprise,on_delete=models.SET_NULL, null=True, blank=True,related_name='comptables', verbose_name="Entreprise")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

