from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_prod', 'nombre', 'id_cate', 'precio', 'descripcion', 'stock', 'imagen']