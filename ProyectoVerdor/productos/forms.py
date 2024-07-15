from django import forms
from .models import Producto,CartItem,User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_prod', 'nombre', 'id_cate', 'precio', 'descripcion', 'stock', 'imagen']

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['name', 'price', 'quantity']

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
