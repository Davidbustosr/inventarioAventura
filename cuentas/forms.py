from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from cuentas.models import Perfil


class RegistroForm(UserCreationForm):
    """Formulario para crear cuenta (UserCreationForm ya valida las 2 contraseñas)."""
    password1 = forms.CharField(label='Contraseña',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir contraseña',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': 'Usuario', 'first_name': 'Nombre', 'last_name': 'Apellido', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class UsuarioEditarForm(forms.ModelForm):
    """Editar un usuario que ya existe (sin cambiar la contraseña)."""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']
        labels = {'username': 'Usuario', 'first_name': 'Nombre', 'last_name': 'Apellido',
                  'email': 'Email', 'is_active': 'Cuenta activa'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['rol', 'telefono']
        labels = {'rol': 'Rol', 'telefono': 'Teléfono'}
        widgets = {
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
