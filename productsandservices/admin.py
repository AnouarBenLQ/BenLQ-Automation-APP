from django.contrib import admin
from .models import Produit,Categorie,SousCategorie,Service,PackProduct,Pack,Promotion

@admin.register(Produit)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['reference','designation','prix_1']

@admin.register(Categorie)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['nom']

@admin.register(SousCategorie)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['nom']

@admin.register(Service)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['designation','prix_ttc_1']
    
@admin.register(PackProduct)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['pack','product','quantity']

@admin.register(Pack)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['nom']


@admin.register(Promotion)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['nom','produit','date_debut','date_fin',]

# Register your models here.
