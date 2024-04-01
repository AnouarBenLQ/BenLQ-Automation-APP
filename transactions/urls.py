from django.urls import path
from . import views

app_name="transactions"

urlpatterns = [

path('transactions/', views.index, name='transactions'),
path('transactions/addinvoice', views.add_invoice, name='addinvoice'),
path('transactions/transactions/newinvoice/<int:client>/<str:date>/', views.new_invoice, name='newinvoice'),
path('transactions/addinvoice_row/', views.add_invoice_row, name='addinvoicerow'),
path('transactions/addinvoice_row/products', views.search_product, name='get_product'),
path('transactions/addinvoice_row/clear', views.clear_component, name='clear'),

]