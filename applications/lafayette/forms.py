from django import forms
from .models import Amigo,Contacto
import datetime



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
            )
        }

    def clean_cliente(self):
        cliente = self.cleaned_data['cliente']

        if not cliente.isalpha() :
            raise forms.ValidationError('Este campo solo puede contener texto')
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

        if not titulo.isalpha() :
            raise forms.ValidationError('Este campo solo puede contener texto')
        return titulo

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']

        if not telefono.isdigit() :
            raise forms.ValidationError('Este campo solo puede contener números')
        return telefono

class Contactoform(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('__all__')
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        if not nombre.isalpha() :
            raise forms.ValidationError('Este campo solo puede contener texto')
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']

        if not telefono.isdigit() :
            raise forms.ValidationError('Este campo solo puede contener números')
        return telefono