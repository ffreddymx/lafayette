from django.contrib import admin
from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
   path('inicio/', views.InicioView.as_view(),name='inicio'),


   path('', views.Index2View,name='index1'),
   path('contacto/', views.ContactoCreateView.as_view(),name='contacto'),

   path('addcliente/', views.ClienteCreateView.as_view(),name='addcliente'),
   path('updatecliente/<pk>/', views.ClienteUpdate.as_view(),name='updatecliente'),
   path('finventa/<pk>/', views.FinVenta,name='finventa'),
   path('tablacliente/', views.listaClientes,name='tablacliente'),

   path('ventacompra/', views.listaVentaCompra,name='ventacompra'),

   path('qsomos/',views.Qsomos.as_view(),name='qsomos'),
]
