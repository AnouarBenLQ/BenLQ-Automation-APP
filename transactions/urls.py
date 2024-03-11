from django.urls import path
from . import views

app_name="transactions"

urlpatterns = [

path('transactions/', views.index, name='transactions'),
path('transactions/addinvoice', views.add_invoice, name='addinvoice'),

]