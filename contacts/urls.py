from django.urls import path
from . import views

app_name="contacts"

urlpatterns = [
    path('clients/', views.index, name='clients'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('prospects/', views.prospects, name='prospects'),
    path('commercials/', views.commercials, name='commercials'),
    path('clients/add/', views.add_client, name='addclient'),
    path('suppliers/add/', views.add_supplier, name='addsupplier'),
    path('prospects/add/', views.add_prospect, name='addprospect'),
    path('commercials/add/', views.add_commercial, name='addcommercial'),
    
]
