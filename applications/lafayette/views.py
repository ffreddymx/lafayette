from django.shortcuts import render, redirect
from django.views.generic import CreateView,UpdateView,TemplateView,ListView,FormView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages

from .models import Amigo,Contacto,Prospecto
from .forms import Amigoform,Contactoform,Prospectoform
from django.contrib.auth import get_user_model

# Create your views here.
# Q(proyecto__icontains=nombre) | Q(sede__icontains=nombre) 

def Index2View(request):
    productosx = Amigo.objects.filter(Q(publicar__icontains=1) and Q(finalizada__icontains=False) )
    nombres = productosx

    if request.POST.get('kword'):
        nombre = request.POST.get('kword')
        nombres = productosx.filter(color__icontains=nombre).order_by('color')
    
    paginator = Paginator(nombres, 4)  
    page = request.GET.get('page')
    users = paginator.get_page(page)

    return render(request, 'index1.html', {'nombres':nombres,'users':users})

#class Index2View(TemplateView):
    #template_name = 'index1.html'
    #login_url = reverse_lazy('login_app:login')


##################################
class InicioView(LoginRequiredMixin,TemplateView):
    template_name = 'inicio.html'
    login_url = reverse_lazy('login_app:login')

class Qsomos(TemplateView):
    template_name = 'qsomos.html'
######################################  DAtos de otros contactos

class RegistrarCreateView(LoginRequiredMixin,CreateView):
    template_name = "cliente/registrar.html"

    model = Contacto
    form_class = Contactoform
    success_url = reverse_lazy('app:ventacompra')

    def form_valid(self, form):
        alumnos = form.save(commit = False)
        alumnos.user = self.request.user
        alumnos.save()
        return super(RegistrarCreateView, self).form_valid(form)

    login_url = reverse_lazy('login_app:login')


class RegistrarUpdate(UpdateView):
    template_name = "cliente/registrar.html"
    model = Contacto
    fields = [ 
        'nombre',
        'telefono',
        'opcion',
        'datos',
        'email',
        'tipo',
        'municipio',
        'estado',
        'colonia',
        'calle',
        'cp',
    ]
    success_url = reverse_lazy('app:ventacompra')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, ** kwargs)

class RegistrarDeleteView(DeleteView):
    model = Contacto
    template_name = "cliente/borrar_registro.html"
    success_url = reverse_lazy('app:ventacompra')





class ContactoCreateView(CreateView):#aqui el problema
    template_name = "ventas/vender.html"
    model = Contacto
    form_class = Contactoform
    success_url = reverse_lazy('app:index1')

    def form_valid(self, form):
        alumnos = form.save(commit = False)
        alumnos.user = self.request.user
        alumnos.save()
        return super(ContactoCreateView, self).form_valid(form)

    login_url = reverse_lazy('login_app:login')


def listaVentaCompra(request):

    if request.user.is_staff: 
        productosx = Contacto.objects.all().order_by('nombre')
    else:
        productosx = Contacto.objects.filter(user = request.user).order_by('nombre')

    nombres = productosx

    if request.POST.get('kword'):
        nombre = request.POST.get('kword')
        nombres = productosx.filter(nombre__icontains=nombre).order_by('cliente')
    
    paginator = Paginator(nombres, 8)  
    page = request.GET.get('page')
    users = paginator.get_page(page)

    return render(request, 'ventas/tabla_vender.html', {'nombres':nombres,'users':users})

######################################  PROSPECTO ####################################################################### PROSPECTO
class ProspectoCreateView(LoginRequiredMixin,CreateView):
    template_name = "prospecto/add_prospecto.html"
    model = Prospecto
    form_class = Prospectoform
    success_url = reverse_lazy('app:tablaprospecto')

    def form_valid(self, form):
        alumnos = form.save(commit = False)
        alumnos.user = self.request.user
        alumnos.save()
        return super(ProspectoCreateView, self).form_valid(form)

    login_url = reverse_lazy('login_app:login')


def listaProspecto(request):

    if request.user.is_staff: 
        productosx = Prospecto.objects.all().order_by('nombre')
    else:
        productosx = Prospecto.objects.filter(user = request.user).order_by('nombre')

    nombres = productosx

    if request.POST.get('kword'):
        nombre = request.POST.get('kword')
        nombres = productosx.filter(cliente__icontains=nombre).order_by('cliente')
    
    paginator = Paginator(nombres, 4)  
    page = request.GET.get('page')
    users = paginator.get_page(page)

    return render(request, 'prospecto/tabla_prospecto.html', {'nombres':nombres,'users':users})


class ProspectoUpdate(UpdateView):
    template_name = "prospecto/add_prospecto.html"
    model = Prospecto
    fields = [ 
        'nombre',
        'telefono',
        'fechac',            
        'fechap',            
        'fechai',
        'interesado',
        'inscrito',
        'contactado',
    ]
    success_url = reverse_lazy('app:tablaprospecto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, ** kwargs)


class ProspectoDeleteView(DeleteView):
    model = Prospecto
    template_name = "prospecto/borrar_prospecto.html"
    success_url = reverse_lazy('app:tablaprospecto')


##xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  REFERIR CLIENTES
class ClienteCreateView(LoginRequiredMixin,CreateView):
    template_name = "cliente/add_cliente.html"
    model = Amigo
    form_class = Amigoform
    success_url = reverse_lazy('app:tablacliente')

    def form_valid(self, form):
        alumnos = form.save(commit = False)
        alumnos.user = self.request.user
        alumnos.save()
        return super(ClienteCreateView, self).form_valid(form)

    login_url = reverse_lazy('login_app:login')



class ClienteUpdate(UpdateView):
    template_name = "cliente/add_cliente.html"
    model = Amigo
    fields = [ 
        'cliente',
        'operacion',
        'producto',
        'municipio',
        'estado',
        'email',
        'telefono',
        'opcion',            
        'titulo',            
        'img',
        'publicar',
        'precio',
        'nota',
    ]
    success_url = reverse_lazy('app:tablacliente')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, ** kwargs)

class ClienteDeleteView(DeleteView):
    model = Amigo
    template_name = "cliente/borrar_referido.html"
    success_url = reverse_lazy('app:tablacliente')


def listaClientes(request):

    if request.user.is_staff: 
        productosx = Amigo.objects.filter(finalizada__icontains=False)
    else:
        productosx = Amigo.objects.filter( Q(user = request.user) & Q(finalizada__icontains=False) )

    #productosx = Amigo.objects.all().order_by('cliente')
    nombres = productosx

    if request.POST.get('kword'):
        nombre = request.POST.get('kword')
        nombres = productosx.filter(cliente__icontains=nombre).order_by('cliente')
    
    paginator = Paginator(nombres, 4)  
    page = request.GET.get('page')
    users = paginator.get_page(page)

    return render(request, 'cliente/tabla_clientes.html', {'nombres':nombres,'users':users})


def FinVenta(request, pk):

    alumnos = Amigo.objects.get(id=pk)    
    #pagosx = Pagos.objects.filter(alumnos_id=pk).order_by('id').reverse() 
    #objetos = pagosx.all()    

    #form  = ColegiaturasForm()
    if request.method == 'POST':

        if alumnos.finalizada == False: 
            User = get_user_model()
            valor = request.POST.get('valor')
            obj = User.object.get(username = request.user)
            obj.ventas = obj.ventas + float(valor)
            obj.save()

            obj = Amigo.objects.get(id = pk)
            obj.finalizada = True
            obj.save()

            messages.info(request,'Este Inmueble se finalizo con Exito... !!')

            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
#,'form':form,'Pagosz':objetos
    context = {'alumnos':alumnos} 
    return render(request, 'cliente/fin_venta.html', context)

