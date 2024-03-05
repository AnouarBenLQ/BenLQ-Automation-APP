from django.contrib import admin
from .models import Client,Fournisseur,Prospect,Commercial

# Register your models here.
@admin.register(Client)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['raison_sociale','type_societe']
    
@admin.register(Fournisseur)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['raison_sociale','type_societe']
    
@admin.register(Prospect)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['raison_sociale','type_societe']

@admin.register(Commercial)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['nom','prenom']