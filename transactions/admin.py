from django.contrib import admin
from .models import Devis

# Register your models here.
@admin.register(Devis)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ['numero','reference','objet','client','suivi_par']