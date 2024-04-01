from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import DevisClient,InformationDevis,ConditiondeVente,LigneDevisForm
from contacts.models import Client
from productsandservices.models import Produit
from accounts.models import CustomUser
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
    if request.method == 'POST':
        form1 = InformationDevis(request.POST, prefix='form1')
        form2 = ConditiondeVente(request.POST, prefix='form2')
        #related_form = LigneDevis(request.POST, prefix='form3')
        
    company=Entreprise.objects.get(pk=1)
    initial_date = datetime.strptime(date, '%Y-%m-%d')
    due_date = initial_date + timedelta(days=30)
    due_date=due_date.strftime('%Y-%m-%d')
    print(date)
    client_obj=Client.objects.get(pk=client)
    print(client_obj)
    form=InformationDevis(initial={'client': client_obj,'date':initial_date,'suivi_par':request.user},prefix='form1')
    form_two=ConditiondeVente(prefix='form2')
    form_three=LigneDevisForm(prefix='form3')
    return render(request,"transactions/add_invoice.html",{'date':date,'form':form,'form_two':form_two,'entreprise':company,})

def add_invoice_row(request):
    if request.method=='POST':
        product_id=request.POST.get('product_id')
        product=Produit.objects.get(pk=product_id)
        context={'product':product}
        return render(request,"transactions/partials/invoice_row.html",context)
    return render(request,"transactions/partials/invoice_row.html")

def search_product(request):
    print("Hello")
    product=request.POST.get('designation')
    results=Produit.objects.filter(designation__icontains=product)
    print(results)
    context={'results':results}
    return render(request,"transactions/partials/search_dropdown.html",context)

def clear_component(request):
    return HttpResponse("")