from django.contrib import admin
from .models import Categoria, Producto, CartItem, User

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(CartItem)
admin.site.register(User)