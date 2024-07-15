from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Producto,Categoria,CartItem,User
# Create your views here.

def semillas(request):
  productos= Producto.objects.raw('SELECT * FROM productos_producto WHERE id_prod <= 6')
  context={"productos":productos}
  return render(request, 'semillas.html', context)

def tierra(request):
  productos= Producto.objects.raw('SELECT * FROM productos_producto WHERE id_prod between "07" and "09" ')
  context={"productos":productos}
  return render(request, 'tierra.html', context)

def herramientas(request):
  productos= Producto.objects.raw('SELECT * FROM productos_producto WHERE id_prod between "013" and "018" ')
  context={"productos":productos}
  return render(request, 'herramientas.html', context)
  
def maceteros(request):
  productos= Producto.objects.raw('SELECT * FROM productos_producto WHERE id_prod >= "019" ')
  context={"productos":productos}
  return render(request, 'maceteros.html', context)
  

def save_cart(request):
  if request.method == 'POST':
    cart_items = request.POST.getlist('cart_items')
    for item in cart_items:
      name, price, quantity = item.split(',')
      CartItem.objects.create(name=name, price=float(price), quantity=int(quantity))
    return JsonResponse({'status': 'success'})
  return JsonResponse({'status': 'failed'})


def inicio(request):
  productos= Producto.objects.all()
  context={"productos":productos}
  return render(request, 'inicio.html', context)


def login(request):
    return render(request, 'login.html')

def crud(request):
    return render(request, 'usuarios_listar.html')

def registro(request):  
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            correo_user = form.cleaned_data.get("correo")
            messages.success(request, 'Usuario guardado con exito')
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html')


def home(request):
    context = {}
    return render(request, 'home.html', context)