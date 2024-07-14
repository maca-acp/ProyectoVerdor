from django.shortcuts import render

from .models import Producto,Categoria
# Create your views here.



def semillas(request):
  productos= Producto.objects.raw('SELECT * FROM productos_producto WHERE id_prod <= 06')
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
  


#def listadoSQL(request):
  #productos= Producto.objects.raw('SELECT * FROM productos_producto')
  #print(productos)
  #context={"productos":productos}
  #return render(request, 'productos/listadoSQL.html', context)
