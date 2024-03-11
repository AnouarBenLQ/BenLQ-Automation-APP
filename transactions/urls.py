from django.urls import path
from . import views

app_name="transactions"

urlpatterns = [

path('transactions/', views.index, name='transactions'),
path('transactions/addinvoice', views.add_invoice, name='addinvoice'),
path('transactions/transactions/newinvoice/<int:client>/<str:date>/', views.new_invoice, name='newinvoice'),

]