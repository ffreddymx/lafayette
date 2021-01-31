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

class Contactoform(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('__all__')
