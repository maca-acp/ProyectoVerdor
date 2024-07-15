from django.shortcuts import render

from .models import Producto,Categoria,CartItem
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