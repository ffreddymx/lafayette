from django.contrib import admin
from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
   path('inicio/', views.InicioView.as_view(),name='inicio'),


   path('', views.Index2View,name='index1'),
   path('contacto/', views.ContactoCreateView.as_view(),name='contacto'),
   path('registrar/', views.RegistrarCreateView.as_view(),name='registrar'),

   path('addcliente/', views.ClienteCreateView.as_view(),name='addcliente'),
   path('updatecliente/<pk>/', views.ClienteUpdate.as_view(),name='updatecliente'),
   path('borrarcliente/<pk>/', views.ClienteDeleteView.as_view(),name='borrarcliente'),

   path('finventa/<pk>/', views.FinVenta,name='finventa'),
   path('tablacliente/', views.listaClientes,name='tablacliente'),

   path('ventacompra/', views.listaVentaCompra,name='ventacompra'),
   path('updateregistrar/<pk>/', views.RegistrarUpdate.as_view(),name='updateregistrar'),
    path('borrarregistro/<pk>/', views.RegistrarDeleteView.as_view(),name='borrarregistro'),

   path('qsomos/',views.Qsomos.as_view(),name='qsomos'),
]
