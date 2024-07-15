from django import forms
from . models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'correo',
            'contraseña',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'rut',
            'telefono',
        ] 
