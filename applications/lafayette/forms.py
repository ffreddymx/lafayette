from django import forms
from .models import Amigo,Contacto,Prospecto
import datetime



class DateInput(forms.DateInput):
    input_type = 'date'


#título de lo que desea
class Amigoform(forms.ModelForm):
    class Meta:
        model = Amigo
        fields = (
            'user',
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
            'nota',)
        widgets = {
            'nota':forms.Textarea(
                attrs={
                    'placeholder':'Descripción del inmueble',
                    'rows':'2',
                }
            ),
            'titulo':forms.TextInput(
                attrs={
                    'placeholder':'Título de lo que desea',
                }
            )
        }

    def clean_cliente(self):
        cliente = self.cleaned_data['cliente']

        x = cliente.split()

        for da in x:
            if not da.isalpha():
                raise forms.ValidationError('Este campo solo puede contener texto')

        #if not cliente.isalpha() :
        #    raise forms.ValidationError('Este campo solo puede contener texto')
        return cliente

    def clean_municipio(self):
        municipio = self.cleaned_data['municipio']

        if not municipio.isalpha() :
            raise forms.ValidationError('Este campo solo puede contener texto')
        return municipio

    def clean_estado(self):
        estado = self.cleaned_data['estado']

        if not estado.isalpha() :
            raise forms.ValidationError('Este campo solo puede contener texto')
        return estado

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']

        x = titulo.split()

        for da in x:
            if not da.isalpha():
                raise forms.ValidationError('Este campo solo puede contener texto')
        return titulo

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']

        if not telefono.isdigit() :
            raise forms.ValidationError('Este campo solo puede contener números')
        return telefono




class Contactoform(forms.ModelForm):#aqui el problema
    class Meta:
        model = Contacto
        fields = ('__all__')
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        x = nombre.split()

        for da in x:
            if not da.isalpha():
                raise forms.ValidationError('Este campo solo puede contener texto')
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']

        if not telefono.isdigit() :
            raise forms.ValidationError('Este campo solo puede contener números')
        return telefono

    def clean_cp(self):
        cp = self.cleaned_data['cp']

        if not cp.isdigit() :
            raise forms.ValidationError('Este campo solo puede contener números')
        return cp


    def clean_municipio(self):
        municipio = self.cleaned_data['municipio']

        if not municipio.isalpha() :
            raise forms.ValidationError('Este campo solo puede contener texto')
        return municipio

    def clean_estado(self):
        estado = self.cleaned_data['estado']

        if not estado.isalpha() :
            raise forms.ValidationError('Este campo solo puede contener texto')
        return estado

    def clean_colonia(self):
        colonia = self.cleaned_data['colonia']

        if not colonia.isalpha() :
            raise forms.ValidationError('Este campo solo puede contener texto')
        return colonia
 





class Prospectoform(forms.ModelForm):
    class Meta:
        model = Prospecto
        fields = ('__all__')

        widgets = {'fechai':DateInput,'fechac':DateInput,'fechap':DateInput,}
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']

        if not telefono.isdigit() :
            raise forms.ValidationError('Este campo solo puede contener números')
        return telefono

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        x = nombre.split()

        for da in x:
            if not da.isalpha():
                raise forms.ValidationError('Este campo solo puede contener texto')
        return nombre