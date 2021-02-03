from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .forms import RegistroUserForm, LoginForm
from django.views.generic import View,DeleteView,UpdateView
from django.views.generic.edit import (
    FormView
)
from .models import User

class RegistroUserView(FormView):
    template_name = 'usuario/add_socio.html'
    form_class = RegistroUserForm
    #success_url = 'uiet_app:inicio'
    success_url = reverse_lazy('login_app:listuser')


    def form_valid(self, form):

        User.object.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['pasword1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
        )

        return super(RegistroUserView, self).form_valid(form)


class LoginUser(FormView):

    template_name = 'index.html'
    form_class = LoginForm
    success_url = reverse_lazy('app:inicio')
    #success_url = '/'

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class UserUpdate(UpdateView):
    template_name = "usuario/update_socio.html"
    model = User
    fields = [ 
        'username',
        'email',
        'nombres',
        'apellidos',
        'municipio',
        'estado',
        'genero',
    ]
    success_url = reverse_lazy('login_app:listuser')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, ** kwargs)



    
class SalirView(View):
    def get(self, request, *args, ** kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'app:index1'
            ) 
        )


def listaUsuarios(request):
    productosx = User.object.all().order_by('nombres')
    nombres = productosx

    if request.POST.get('kword'):
        nombre = request.POST.get('kword')
        nombres = productosx.filter(nombres__icontains=nombre).order_by('nombres')
    
    paginator = Paginator(nombres, 4)  
    page = request.GET.get('page')
    users = paginator.get_page(page)

    return render(request, 'usuario/tabla_socios.html', {'nombres':nombres,'users':users})


class UserDeleteView(DeleteView):
    model = User
    template_name = "usuario/borrar_user.html"
    success_url = reverse_lazy('login_app:listuser')

