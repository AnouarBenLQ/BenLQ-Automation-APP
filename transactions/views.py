from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import DevisForm,DevisClient,InformationDevis
from contacts.models import Client
from coreApp.models import Entreprise
from datetime import date, datetime, timedelta

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
    
    form=DevisClient()
    context = {'nav_tabs': nav_tabs,'form':form,'url': reverse('transactions:addinvoice')}
    return render(request, 'transactions/transactions.html', context)

def add_invoice(request):
    
    if request.method == 'POST':
        client=request.POST.get("client")
        date=request.POST.get("date")
        print(client,date)
        url = reverse('transactions:newinvoice', kwargs={'client': client, 'date': date})
        return redirect(url)
    
    context = {'nav_tabs': nav_tabs,}
    return render(request, 'transactions/add_invoice.html', context)

def new_invoice(request,client, date):
    company=Entreprise.objects.get(pk=1)
    initial_date = datetime.strptime(date, '%Y-%m-%d')
    due_date = initial_date + timedelta(days=30)
    due_date=due_date.strftime('%Y-%m-%d')
    print(date)
    client_obj=Client.objects.get(pk=client)
    print(client_obj)
    client_name=client_obj.nom
    form=InformationDevis()
    return render(request,"transactions/add_invoice.html",{'date':date,'form':form,'client':client_obj,'entreprise':company,'due_date':due_date})