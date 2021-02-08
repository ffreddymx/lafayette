from django import forms

from .models import User
from django.contrib.auth import authenticate

class RegistroUserForm(forms.ModelForm):

    pasword1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    pasword2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )


    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
            'municipio',
            'estado',
            )
    
    def clean_password2(self):
        if self.cleaned_data['pasword1'] != self.cleaned_data['pasword2']:
            self.add_error('pasword2', 'Las contraseña no son iguales...')

    def clean_nombres(self):
        nombres = self.cleaned_data['nombres']

        x = nombres.split()

        for da in x:
            if not da.isalpha():
                raise forms.ValidationError('Este campo solo puede contener texto')
        return nombres

    def clean_apellidos(self):
        apellidos = self.cleaned_data['apellidos']

        x = apellidos.split()

        for da in x:
            if not da.isalpha():
                raise forms.ValidationError('Este campo solo puede contener texto')

        return apellidos

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


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nombre de Usuario',
                'style':'{margin:10px}',
                'class':'form-control input_user'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña',
                'class':'form-control input_user',

            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los Datos no son correctos')
        return self.cleaned_data


