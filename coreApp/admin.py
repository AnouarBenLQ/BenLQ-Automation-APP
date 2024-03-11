from django.contrib import admin
from.models import Entreprise

# Register your models here.
@admin.register(Entreprise)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['raison_sociale','email','logo']
    
