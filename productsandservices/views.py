from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from .forms import ProductForm,ServiceForm,PackProductForm,CategoryForm,SubcategoryForm,PromotionForm
from .models import Pack,PackProduct,Produit
from django.contrib import messages


# Create your views here.
nav_tabs = [
        {'id': 2, 'label': 'Produits'},
        {'id': 3, 'label': 'Services'},
        {'id': 4, 'label': 'Packs'},
        {'id': 5, 'label': 'Categories'},
        {'id': 6, 'label': 'Promotions'},
        # Add more tabs as needed
    ]

    
@login_required
def index(request):
    
    context = {'nav_tabs': nav_tabs,'menu':'Produits','url': reverse('productsandservices:addproduct')}
    return render(request, 'products/products.html', context)

@login_required
def services(request):
    
    context = {'nav_tabs': nav_tabs,'menu':'Services','url': reverse('productsandservices:addservice')}
    return render(request, 'products/products.html', context)

@login_required
def categories(request):
    
    context = {'nav_tabs': nav_tabs,'menu':'Catégories','showformButton':True,'url': reverse('productsandservices:addcategory')}
    return render(request, 'products/categories.html', context)

@login_required
def packs(request):
    
    context = {'nav_tabs': nav_tabs,'menu':'Packs','url': reverse('productsandservices:addpack')}
    return render(request, 'products/products.html', context)

@login_required
def promotions(request):
    
    context = {'nav_tabs': nav_tabs,'menu':'Promotions','showformButton':False,'url': reverse('productsandservices:addpromotion')}
    return render(request, 'products/products.html', context)

def add_product(request):
    
    current_user_entreprise = request.user.entreprise
    print(current_user_entreprise)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, user=request.user)
        if form.is_valid():
            
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.entreprise = current_user_entreprise
            record.save()
            messages.success(request, f"Produit {record.designation} est ajouté avec succès !")
            return render(request, 'products/add_product.html', {'form':ProductForm(),'title':'Nouveau Produit','showToast':True,'nav_tabs': nav_tabs})
            
            
        else:
            print("form is invalid")
            print(form.errors)
            client_creation_form = ProductForm(request.POST,user=request.user)
            context = {'form': client_creation_form,'nav_tabs': nav_tabs,'title':'Nouveau Produit'}
            return render(request, 'products/add_product.html', context)
            
   
    client_creation_form = ProductForm()
    
    context = {'form': client_creation_form,'nav_tabs': nav_tabs,'showToast':False,'title':'Nouveau Produit'}
    return render(request, 'products/add_product.html', context)

def add_service(request):
    
    current_user_entreprise = request.user.entreprise
    print(current_user_entreprise)
    if request.method == 'POST':
        form = ServiceForm(request.POST, user=request.user)
        if form.is_valid():
            
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.entreprise = current_user_entreprise
            record.save()
            messages.success(request, f"Service {record.designation} est ajouté avec succès !")
            return render(request, 'products/add_service.html', {'form':ServiceForm(),'title':'Nouveau Service','showToast':True,'nav_tabs': nav_tabs})
            
            
        else:
            print("form is invalid")
            print(form.errors)
            form = ServiceForm(request.POST,user=request.user)
            context = {'form': form,'nav_tabs': nav_tabs,'title':'Nouveau Service'}
            return render(request, 'products/add_service.html', context)
            
   
    form = ServiceForm()
    
    context = {'form': form,'nav_tabs': nav_tabs,'showToast':False,'title':'Nouveau Service'}
    return render(request, 'products/add_service.html', context)

def add_pack(request):
    
    current_user_entreprise = request.user.entreprise
    print(current_user_entreprise)
    if request.method == 'POST':
        print(request.POST)
       
        form = PackProductForm(request.POST)
        if form.is_valid():
            new_pack_name = form.cleaned_data['new_pack_name']
            pack, created = Pack.objects.get_or_create(nom=new_pack_name)
            products = request.POST.getlist('product')
            quantities = request.POST.getlist('quantity')
            for i in range(len(products)):
                product_id = products[i]
                product = Produit.objects.get(id=product_id)
                quantity = quantities[i]
                pack_product = PackProduct.objects.create(pack=pack, product=product, quantity=quantity)
                pack_product.save()
            messages.success(request, f"Pack {new_pack_name} est ajouté avec succès !")
            return render(request, 'products/add_pack.html', {'form':PackProductForm(),'title':'Nouveau Pack Produit','showToast':True,'nav_tabs': nav_tabs})
            
            
        else:
            print("form is invalid")
            print(form.errors)
            form = PackProductForm(request.POST)
            context = {'form': form,'nav_tabs': nav_tabs,'title':'Nouveau Pack Produit'}
            return render(request, 'products/add_pack.html', context)
            
   
    form = PackProductForm()
    
    context = {'form': form,'nav_tabs': nav_tabs,'showToast':False,'title':'Nouveau Pack Produit'}
    return render(request, 'products/add_pack.html', context)

def add_productpack(request):
    
    form = PackProductForm()
    context = {'form': form,}
    return render(request, 'products/form_snippet.html', context)
    
def add_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.save()
            messages.success(request, f"Catégorie {record.nom} est ajouté avec succès !")
            return render(request, 'products/categories.html', {'form':CategoryForm(),'showToast':True,'nav_tabs': nav_tabs,'menu':'Catégories','showformButton':True,'url':reverse('productsandservices:addcategory')})
  
        else:
            print("form is invalid")
            print(form.errors)
            form = CategoryForm(request.POST,user=request.user)
            context = {'form': form,'nav_tabs': nav_tabs,'title':'Nouvelle Catégorie'}
            return render(request, 'contacts/contacts.html', context)
            
   
    form = CategoryForm()
    
    context = {'form': form,'nav_tabs': nav_tabs,'title':'Nouvelle Catégorie'}
    return render(request, 'products/categoryForm.html', context)

def add_subcategory(request):
    
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.save()
            messages.success(request, f"Sous-catégorie {record.nom} est ajouté avec succès !")
            return render(request, 'products/categories.html', {'form':SubcategoryForm(),'showToast':True,'nav_tabs': nav_tabs,'menu':'Catégories','showformButton':True,'url':reverse('productsandservices:add_subcategory')})
  
        else:
            print("form is invalid")
            print(form.errors)
            form = SubcategoryForm(request.POST,user=request.user)
            context = {'form': form,'nav_tabs': nav_tabs,'title':'Nouvelle Catégorie'}
            return render(request, 'contacts/contacts.html', context)
            
   
    form = SubcategoryForm()
    
    context = {'form': form,'nav_tabs': nav_tabs,'title':'Nouvelle Sous-catégorie'}
    return render(request, 'products/SubcategoryForm.html', context)

def add_promotion(request):
    
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            # Assign the entreprise of the current user to the BaseEntity instance
            record = form.save(commit=False)
            record.save()
            messages.success(request, f"Sous-catégorie {record.nom} est ajouté avec succès !")
            return render(request, 'products/categories.html', {'form':PromotionForm(),'showToast':True,'nav_tabs': nav_tabs,'menu':'Catégories','showformButton':True,'url':reverse('productsandservices:addpromotion')})
  
        else:
            print("form is invalid")
            print(form.errors)
            form = PromotionForm(request.POST,user=request.user)
            context = {'form': form,'nav_tabs': nav_tabs,'title':'Nouvelle Catégorie'}
            return render(request, 'contacts/contacts.html', context)
            
   
    form = PromotionForm()
    
    context = {'form': form,'nav_tabs': nav_tabs,'title':'Nouvelle Sous-catégorie'}
    return render(request, 'products/add_promotion.html', context)