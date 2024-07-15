from django.shortcuts import render, redirect
from .models import User
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def index(request):
    context={}
    return render(request, 'verdoapp/Vista_inicio.html', context)

def login(request):
    return render(request, 'verdoapp/login.html')

def crud(request):
    return render(request, 'verdoapp/usuarios_listar.html')

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
    return render(request, 'verdoapp/registro.html')

def home(request):
    context = {}
    return render(request, 'verdoapp/home.html', context)
