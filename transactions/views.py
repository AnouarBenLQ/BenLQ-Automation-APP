from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import DevisForm

# Create your views here.
nav_tabs = [
        {'id': 2, 'label': 'Devis'},
        {'id': 3, 'label': 'Commandes'},
        {'id': 4, 'label': 'Factures'},
        {'id': 5, 'label': 'Livraisons'},
        {'id': 6, 'label': 'Retour Client'},
        # Add more tabs as needed
    ]

@login_required
def index(request):
    
    form=DevisForm()
    context = {'nav_tabs': nav_tabs,'menu':'Devis','form':form,'url': reverse('transactions:addinvoice')}
    return render(request, 'transactions/transactions.html', context)

def add_invoice(request):
    
    
    context = {'nav_tabs': nav_tabs,}
    return render(request, 'transactions/add_invoice.html', context)