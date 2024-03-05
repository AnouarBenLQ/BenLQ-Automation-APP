from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SupplierCreationForm,ClientCreationForm,ProspectCreationForm,CommercialForm

# Create your views here.
nav_tabs = [
        {'id': 2, 'label': 'Clients'},
        {'id': 3, 'label': 'Fournisseurs'},
        {'id': 4, 'label': 'Prospects'},
        {'id': 5, 'label': 'Commerciaux'},
        # Add more tabs as needed
    ]

    
@login_required
def index(request):
    
    context = {'nav_tabs': nav_tabs,'client_type':'clients','url': reverse('contacts:addclient')}
    return render(request, 'contacts/contacts.html', context)

@login_required
def suppliers(request):
    
    context = {'nav_tabs': nav_tabs,'client_type':'fournisseurs','url':reverse('contacts:addsupplier')}
    return render(request, 'contacts/contacts.html', context)

@login_required
def prospects(request):
    
    context = {'nav_tabs': nav_tabs,'client_type':'prospects','url':reverse('contacts:addprospect')}
    return render(request, 'contacts/contacts.html', context)

@login_required
def commercials(request):
    
    client_creation_form = CommercialForm()
    
    context = {'nav_tabs': nav_tabs,'form': client_creation_form,'client_type':'Commerciaux','showformButton':True}
    return render(request, 'contacts/contacts.html', context)


def add_client(request):
    
    current_user_entreprise = request.user.entreprise
    print(current_user_entreprise)
    if request.method == 'POST':
        form = ClientCreationForm(request.POST,request.FILES, user=request.user)
        if form.is_valid():
            
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.entreprise = current_user_entreprise
            record.save()
            return render(request, 'contacts/add_client.html', {'form':ClientCreationForm(),'title':'Nouveau Client','client_type':'Client','client':record.raison_sociale,'showModal':True,'nav_tabs': nav_tabs})
            
            
        else:
            print("form is invalid")
            print(form.errors)
            client_creation_form = ClientCreationForm(request.POST,user=request.user)
            context = {'form': client_creation_form,'nav_tabs': nav_tabs,'title':'Nouveau Client'}
            return render(request, 'contacts/add_client.html', context)
            
   
    client_creation_form = ClientCreationForm()
    
    context = {'form': client_creation_form,'nav_tabs': nav_tabs,'showModal':False,'title':'Nouveau Client'}
    return render(request, 'contacts/add_client.html', context)

def add_supplier(request):
    
    current_user_entreprise = request.user.entreprise
    print(current_user_entreprise)
    if request.method == 'POST':
        form = SupplierCreationForm(request.POST,request.FILES, user=request.user)
        if form.is_valid():
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.entreprise = current_user_entreprise
            record.save()
            return render(request, 'contacts/add_client.html', {'form':SupplierCreationForm(),'showModal':True,'client_type':'Fournisseur','client':record.raison_sociale,'nav_tabs': nav_tabs,'title':'Nouveau Fournisseur'})
            
            
        else:
            print("form is invalid")
            print(form.errors)
            client_creation_form = SupplierCreationForm(request.POST,user=request.user)
            context = {'form': client_creation_form,'nav_tabs': nav_tabs,'title':'Nouveau Fournisseur'}
            return render(request, 'contacts/add_client.html', context)
            
   
    client_creation_form = SupplierCreationForm()
    
    context = {'form': client_creation_form,'nav_tabs': nav_tabs,'title':'Nouveau Fournisseur'}
    return render(request, 'contacts/add_client.html', context)

def add_prospect(request):
    
    current_user_entreprise = request.user.entreprise
    print(current_user_entreprise)
    if request.method == 'POST':
        form = ProspectCreationForm(request.POST,request.FILES, user=request.user)
        if form.is_valid():
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.entreprise = current_user_entreprise
            record.save()
            return render(request, 'contacts/add_client.html', {'form':ProspectCreationForm(),'showModal':True,'client_type':'Prospect','client':record.raison_sociale,'nav_tabs': nav_tabs,'title':'Nouveau Prospect'})
            
            
        else:
            print("form is invalid")
            print(form.errors)
            client_creation_form = ProspectCreationForm(request.POST,user=request.user)
            context = {'form': client_creation_form,'nav_tabs': nav_tabs,'title':'Nouveau Prospect'}
            return render(request, 'contacts/add_client.html', context)
            
   
    client_creation_form = ProspectCreationForm()
    
    context = {'form': client_creation_form,'nav_tabs': nav_tabs,'title':'Nouveau Prospect'}
    return render(request, 'contacts/add_client.html', context)

def add_commercial(request):
    
    current_user_entreprise = request.user.entreprise
    print(current_user_entreprise)
    if request.method == 'POST':
        form = CommercialForm(request.POST, user=request.user)
        if form.is_valid():
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.entreprise = current_user_entreprise
            record.save()
            return render(request, 'contacts/contacts.html', {'form':CommercialForm(),'showModal':True,'client_type':'Prospect','nav_tabs': nav_tabs,'title':'Nouveau Commercial'})
            
            
        else:
            print("form is invalid")
            print(form.errors)
            client_creation_form = CommercialForm(request.POST,user=request.user)
            context = {'form': client_creation_form,'nav_tabs': nav_tabs,'title':'Nouveau Commercial'}
            return render(request, 'contacts/contacts.html', context)
            
   
    client_creation_form = CommercialForm()
    
    context = {'form': client_creation_form,'nav_tabs': nav_tabs,'title':'Nouveau Commercial',}
    return render(request, 'core/partials/components/form_modal.html', context)