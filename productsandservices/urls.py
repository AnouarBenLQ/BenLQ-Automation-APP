from django.urls import path
from . import views

app_name="productsandservices"


urlpatterns = [

path('products/', views.index, name='products'),
path('services/', views.services, name='services'),
path('categories/', views.categories, name='categories'),
path('promotions/', views.promotions, name='promotions'),
path('packs/', views.packs, name='packs'),
path('products/add/', views.add_product, name='addproduct'),
path('services/add/', views.add_service, name='addservice'),
path('packs/add/', views.add_pack, name='addpack'),
path('packs/addproductpack/', views.add_productpack, name='addproductpack'),
path('categories/add', views.add_category, name='addcategory'),
path('subcategories/add', views.add_subcategory, name='add_subcategory'),
path('promotions/add', views.add_promotion, name='addpromotion'),
]